from celery import shared_task, task
from .models import Pitchfork_model
from . import scrapper
from datetime import datetime

@task
def get_data_pitchfork(page_number):
    p_scrapper = scrapper.Pitchfork()
    news_list = p_scrapper.get_news(page_number)
    for news in news_list:
        if not Pitchfork_model.objects.filter(headline = news.headline).exists():
            news.get_description()
            news.get_tags()
            noticia = Pitchfork_model(link = news.link, headline = news.headline, description = news.description, date = datetime.strptime(" ".join(news.date.split(" ")[1:4]), "%d %b %Y"))
            noticia.set_tags(news.tags)
            noticia.save()
    
