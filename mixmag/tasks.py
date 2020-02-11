from celery import shared_task, task
from .models import MixMag_model
from . import scrapper
from datetime import datetime

@task
def get_data_mixmag(page_number):
    MixMag_scrapper = scrapper.MixMag()
    news = MixMag_scrapper.get_news(page_number)
    for new in news:
        if not MixMag_model.objects.filter(headline = new.headline).exists():
            new.get_date()
            noticia = MixMag_model(headline = new.headline, link = new.link, description = new.description, date = datetime.strptime(new.date, "%d %B %Y"), category = "news")
            new.get_tags()
            noticia.set_tags(new.tags)
            noticia.save()
    
    tech = MixMag_scrapper.get_tech(page_number)
    for ntech in tech:
        if not MixMag_model.objects.filter(headline = ntech.headline).exists():
            ntech.get_date()
            tnoticia = MixMag_model(headline = ntech.headline, link = ntech.link, description = ntech.description, date = datetime.strptime(ntech.date, "%d %B %Y"), category = "tech")
            ntech.get_tags()
            tnoticia.set_tags(ntech.tags)
            tnoticia.save()