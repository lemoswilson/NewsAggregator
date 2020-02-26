from celery import shared_task, task
from .models import FactMag_model
from . import scrapper
from datetime import datetime

# just to comment
#thrash

@task() 
def get_data_factmag(category, n_of_pages):
    # getting the highlight posts and check if they already exists i the database
    FactMag_scrapper = scrapper.FactMagScrapper()
    highlight = FactMag_scrapper.get_highlight_post(category)
    if not FactMag_model.objects.filter(headline=highlight.headline, link=highlight.link).exists():
        highlight.get_tags()
        highlight.get_description()
        highlight.get_date()
        news_headline = FactMag_model(headline = highlight.headline, link = highlight.link, date = datetime.strptime(highlight.date, "%d.%m.%y"), is_highlight = category[0], category = category, description = highlight.description)
        news_headline.set_tags(highlight.tags)
        news_headline.save()

    # getting posts of the 2 first pages
    for p in range(len(n_of_pages)):
        news_list = FactMag_scrapper.get_posts(category, p)
        # iterating over the news_list
        for news in news_list:
            if not FactMag_model.objects.filter(headline = news.headline).exists():
                news.get_tags()
                news.get_description()
                post = FactMag_model(headline = news.headline, link = news.link, date=datetime.strptime(news.date, "%d.%m.%y"), category=category, is_highlight="0", description = news.description)
                post.set_tags(news.tags)
                post.save()

