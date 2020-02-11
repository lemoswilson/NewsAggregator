from celery import shared_task, task
from .models import ResidentAdvisor_model
from . import scrapper
from datetime import datetime

@task
def get_data_residentadvisor(number_of_days):
    ra_scrapper = scrapper.ResidentAdvisor()
    
    featured_news = ra_scrapper.get_featured_news()
    if not ResidentAdvisor_model.objects.filter(headline = featured_news.headline).exists():
        featured_news.get_date()
        featured_news.get_tags()
        featured_news.get_description()
        featured = ResidentAdvisor_model(link = featured_news.link, description = featured_news.description, headline = featured_news.headline, date = datetime.strptime(featured_news.date[0].strip(), "%d %b %Y"), tags = featured_news.tags, is_featured=True)
        featured.save()

    popular_news = ra_scrapper.get_popular_news()
    for news in popular_news:
        if not ResidentAdvisor_model.objects.filter(headline = news.headline).exists():
            news.get_tags()
            news.get_date()
            news.get_description()
            n_news = ResidentAdvisor_model(link = news.link, description = news.description, headline = news.headline, date = datetime.strptime(news.date[0].strip(), "%d %b %Y"), tags = news.tags, is_featured = False)
            n_news.save()
    
    news_from_date = ra_scrapper.get_news_from_to(number_of_days)
    for news in news_from_date:
        if not ResidentAdvisor_model.objects.filter(headline = news.headline).exists():
            news.get_tags()
            news.get_date()
            news.get_description()
            n_news = ResidentAdvisor_model(link = news.link, description = news.description,  headline = news.headline, date = datetime.strptime(news.date[0].strip(), "%d %b %Y"), tags = news.tags, is_featured = False)
            n_news.save()


