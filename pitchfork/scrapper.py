import requests
from bs4 import BeautifulSoup  
from datetime import datetime
import json


class Pitchfork:
    def __init__(self):
        self.news = "https://pitchfork.com/news/?genre=electronic&page="
        self.base = "https://pitchfork.com"

    def get_news(self, page_number):
        news_list = []
        url = self.news + str(page_number)
        page = requests.get(url)
        content = page.content
        sopa = BeautifulSoup(content, "html.parser")
        news = sopa.find(id="news-page")

        latest_hero = news.find("div", {"class":"latest-hero"}) 
        hero_img = latest_hero.find("img")['src']
        hero_link = self.base + latest_hero.find('a')['href']
        hero_headline = latest_hero.find("h2", {"class":"title"}).text
        hero_description = latest_hero.find("div", {"class":"abstract"}).text
        meta = latest_hero.find("div", {"class":"meta"})
        hero_date = meta.find("time")["title"]
        news_list.append(self.NewsPage(hero_link, img_link = hero_img, headline = hero_headline, description=hero_description, date=hero_date)) 

        second_tier = news.find("section", {"class":"second-tier"})
        second_tier_news = second_tier.find_all("div", {"class":"news-module"})
        for n in second_tier_news:
            news_img = n.find("img")['src']
            news_link = self.base + n.find("a")['href']
            news_headline = n.find("h2", {"class":"title"}).text
            news_date = n.find("time")['title']
            news_list.append(self.NewsPage(news_link, img_link = news_img, headline = news_headline, date = news_date))

        third_tier = news.find("section", {"class":"third-tier"})
        third_tier_news = third_tier.find_all("div", {"class":"news-module"})
        for n in third_tier_news:
            news_img = n.find("img")['src']
            news_link = self.base + n.find("a")['href']
            news_headline = n.find("h2", {"class":"title"}).text
            news_date = n.find("time")['title']
            news_list.append(self.NewsPage(news_link, img_link = news_img, headline = news_headline, date = news_date))

        return news_list


    class NewsPage:
        def __init__(self, link, headline=None, description=None, author=None, date=None, text=None, img_link=None, content_images=None, content_links = None, iframe = None, tags=None, artists=None):
            self.link = link
            self.headline = headline
            self.description = description
            self.author = author
            self.img_link = img_link
            self.date = date
            self.text = text
            self.content_links = content_links
            self.content_images = content_images
            self.iframe = iframe
            self.tags = tags
            self.artists = artists
            self.soup = None    

        def __str__(self):
            return self.headline
        
        def page_soup(self):
            if not self.soup:
                page = requests.get(self.link)
                content = page.content
                soup = BeautifulSoup(content, "html.parser")
                self.soup = soup
            return self.soup

        def article(self):
            return self.page_soup().find("article").find("div", {"class":"article-content"})

        def get_headline(self):
            if not self.headline:
                self.headline = self.article().find("h1").text
            return self.headline
        
        def get_description(self):
            if not self.description:
                self.description = self.article().find("h2").text
            return self.description

        def get_date(self):
            if not self.date:
                self.date = self.article().find("time")["title"] # time format "weekday Mon dd yyyy hh:mm:ss FUSO"
            return self.date
        
        def get_author(self):
            try:
                ul = self.page_soup().find("ul", {"class":"authors-detail"})
                authors = ul.find_all("li")
                self.author = [i.find("a").text for i in authors]
            except:
                div = self.page_soup().find("div", {"class":"authors-detail"})
                authors = div.find_all("a")
                self.author = [i.text for i in authors]
            return self.author
        
        def get_img_link(self):
            if not self.img_link:
                self.img_link = self.article().find("img")['src']
            return self.img_link

        def get_text(self):
            contents = self.article().find("div", {"class":"contents"})
            elements = contents.find_all()
            self.text = "".join([element.text for element in elements if element.name != "figure"])

        def get_content_links(self):
            contents = self.article().find("div", {"class":"contents"})
            if contents.find("a"):
                self.content_links = [i['href'] for i in contents.find_all("a") if i.has_attr("href")]
            return self.content_links
        
        def get_content_images(self):
            contents = self.article().find("div", {"class":"contents"})
            if contents.find("img"):
                self.content_images = [i['src'] for i in contents.find_all("img")if i.has_attr("src")]
            return self.content_images

        def get_iframe(self):
            contents = self.article().find("div", {"class":"contents"})
            if contents.find("iframe"):
                self.iframe = [i['src'] for i in contents.find_all("iframe") if i.has_attr("src")]
            return self.iframe
        
        def get_tags(self):
            aside = self.page_soup().find("aside")
            tag_section = aside.find_all("section")[1]
            tag_list = tag_section.find_all("li")
            self.tags = [i.text for i in tag_list]
            return self.tags

        def get_artists(self):
            aside = self.page_soup().find("aside")
            artists_section = aside.find_all("section")[0]
            artists_list = artists_section.find_all("li")
            self.artists = [i.text for i in artists_list]

        def get_all(self):
            self.get_artists()
            self.get_author()
            self.get_content_images()
            self.get_content_links()
            self.get_date()
            self.get_description()
            self.get_headline()
            self.get_iframe()
            self.get_img_link()
            self.get_tags()
            self.get_text()
            return self

