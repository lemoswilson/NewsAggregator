import requests
from bs4 import BeautifulSoup  
from datetime import datetime
import json
import bs4

class MixMag:
    def __init__(self):
        self.news = 'https://mixmag.net/news/'
        self.base = "https://mixmag.net"
        self.tech = "https://mixmag.net/tech/"

    def get_news(self, page_number):
        news_list = []
        url = self.news + f'p{page_number}'
        page = requests.get(url)
        content = page.content
        soup = BeautifulSoup(content, "html.parser")
        news = soup.find_all("article", {"class":"story-block"})
        for new in news:
            news_link = self.base + new.find("a", {"class":"story-block__clickable"})['href']
            news_img = new.find("img")['src']
            news_headline = new.find("h3", {"class":"story-block__title"}).text
            news_description = new.find("div", {"class":"story-block__excerpt"}).text
            news_list.append(self.NewsPage(news_link, img_link = news_img, description = news_description, headline = news_headline))
        return news_list

    def get_tech(self, page_number):
        news_list = []
        url = self.tech + f'p{page_number}'
        page = requests.get(url)
        content = page.content
        soup = BeautifulSoup(content, "html.parser")
        news = soup.find_all("article", {"class":"story-block"})
        for new in news:
            news_link = self.base + new.find("a", {"class":"story-block__clickable"})['href']
            news_img = new.find("img")['src']
            news_headline = new.find("h3", {"class":"story-block__title"}).text
            news_description = new.find("div", {"class":"story-block__excerpt"}).text
            news_list.append(self.NewsPage(news_link, img_link = news_img, description = news_description, headline = news_headline))
        return news_list


    class NewsPage:
        def __init__(self, link, headline=None, description=None, author=None, date=None, text=None, img_link=None, content_images=None, content_links = None, iframe = None, tags=None, categories=None):
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
            self.categories = categories
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
            else:
                return self.soup

        def is_feature(self):
            return True if self.page_soup().find("section", {"class":"feature-section"}) else False

        def meta(self):
            return self.page_soup().find("ul", {"class":"article-header__meta"}) 

        def get_headline(self):
            self.headline = self.page_soup().find("h1", {"class":"article-header__title"}).text
            return self.headline

        def get_description(self):
            self.description = self.page_soup().find("div", {"class":"article-header__excerpt"}).text
            return self.description

        def get_author(self):
            self.author = self.meta().find_all("li")[0].text
            return self.author
        
        def get_date(self): ## date format = "d Month yyyy"
            self.date = self.meta().find_all("li")[1].text
            if len(self.date.split(" ")[0]) == 1:
                self.date = "0" + self.date
            # after that the date format will be "dd Month yyyy"
            return self.date

        def get_text(self):
            if not self.is_feature():
                div = self.page_soup().find("div", {"class":"rich-text"})
                text = [i.text for i in div.find_all("p") if "Read this next:" not in i.text]
                self.text = "\n".join(text)
            else:
                # self.text = self.page_soup().find("section", {"class":"feature-section"}).text
                section = self.page_soup().find("section", {"class":"feature-section"})
                text_blocks = section.find_all("div", {"class":"rich-text__block"})
                texts = []
                for text_block in text_blocks:
                    for i in text_block.find_all():
                        if i.name != 'style' and "Read this next:" not in i.text:
                            texts.append(i.text)
                        else:
                            continue
                self.text = "".join(texts)
            return self.text

        def get_categorie(self):
            self.categories = self.page_soup().find("a", {"class":"context-marker"}).text
            return self.categories

        def get_tags(self):
            if not self.is_feature():
                ul = self.page_soup().find("ul", {"class":"tags"})
                tags_element = ul.find_all("li", {"class":"tags__tag"})
                self.tags = [i.text for i in tags_element if "Home" not in i.text and "Tech" not in i.text and "News" not in i.text]
            else:
                taglits = self.page_soup().find("article")["data-tags"].split(",")
                self.tags = [i for i in taglits if "Home" not in i and "Tech" not in i and "News" not in i] 
            return self.tags

        def get_img_link(self):
            if not self.is_feature():
                if not self.img_link:
                    self.img_link = self.page_soup().find("img", {"class":"media--cover"})['src']
                else:
                    return self.img_link
            else:
                self.img_link = self.page_soup().find("header", {"class":"article-header"}).find("img")["src"]
                return self.img_link

        def get_content_links(self):
            cl = []
            if not self.is_feature():
                div = self.page_soup().find("div", {"class":"rich-text"})
                paragraphs = [i for i in div.find_all("p") if "Read this next:" not in i.text]
                for p in paragraphs:
                    if p.find("a"):
                        cl.append([i['href'] for i in p.find_all("a")])
                self.content_links = cl
            else:
                section = self.page_soup().find("section", {"class":"feature-section"})
                if section.find("a"):
                    self.content_links = [i['href'] for i in section.find_all("a") if i.has_attr("href")]
            return self.content_links

        def get_content_images(self):
            ci = []
            if not self.is_feature():
                div = self.page_soup().find("div", {"class":"rich-text"})
                if div.find("img"):
                    for i in div.find_all("img"):
                        ci.append(i['src']) 
                self.content_images = ci
            else:
                section = self.page_soup().find("section", {"class":"feature-section"})
                if section.find("img"):
                    self.content_images = [i['src'] for i in section.find_all("img") if i.has_attr("src")]
            return self.content_images
            
        def get_iframe(self):
            i_frame = []
            if not self.is_feature():
                div = self.page_soup().find("div", {'class':"rich-text"})
                if div.find("iframe"):
                    for i in div.find_all("iframe"):
                        i_frame.append(i['src'])
                self.iframe = i_frame
            else:
                section = self.page_soup().find("section", {"class":"feature-section"})
                if section.find("div", {"class":"media__video"}):
                    divs = section.find_all("div", {"class":"media__video"})
                    for media_div in divs:
                        i_frame.append(media_div.find("iframe")['src'])
                    self.iframe = i_frame
            return self.iframe

        def get_all(self):
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

        def to_json(self):
            return json.dumps(self.__dict__)

