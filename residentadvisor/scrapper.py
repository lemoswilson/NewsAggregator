import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime




class ResidentAdvisor:
    def __init__(self):
        self.base = 'https://www.residentadvisor.net'
        self.post_url = "https://www.residentadvisor.net/Output/news-listing-output.aspx"
        self.news_url = 'https://www.residentadvisor.net/news'


    def get_featured_news(self):
        page = requests.get(self.base)
        content = page.content
        content_soup = BeautifulSoup(content, "html.parser")

        # get the featured post informations
        featured_post_html = content_soup.find(id="news").find("article")
        featured_post_image_link = featured_post_html.find("img")['src']
        featured_post_headline = featured_post_html.find("h1", {"class":"f36"}).text
        featured_post_link = featured_post_html.find("a")['href']

        return self.NewsPage(self.base + featured_post_link, img_link=featured_post_image_link, headline = featured_post_headline)


    def get_popular_news(self): # returns a list of NewsPage objects
        page = requests.get(self.news_url)
        content = page.content
        page_soup = BeautifulSoup(content, 'html.parser')
        popular_ul = page_soup.find(id="news-listing").find("ul")
        popular_news = [i for i in popular_ul.find_all("li")]
        list_of_news = []

        for news in popular_news:
            date = news.find("p", {"class":"date"}).text # date format dayoftheweek, dd mon yyyy
            link = news.find("a")['href']
            image_link = news.find("img")['src']
            headline = news.find("h1").text
            description = news.find("p", {"class":"copy"}).text
            list_of_news.append(self.NewsPage(self.base + link, img_link = image_link, headline= headline, description = description, date=date))
        return list_of_news
        

    def get_news_from_to(self, initial_date=datetime.now().strftime("%d/%m/%Y"), n_of_days=7):
        # date format is dd/mm/yyyy
        data = {"date":f'{initial_date}', "days":f'{n_of_days}'}
        chamada = requests.post(self.post_url, data=data)
        chamada_content = chamada.content
        chamadasoup = BeautifulSoup(chamada_content, "html.parser")
        list_of_news = [] # format 
        days = chamadasoup.find_all("li", {"class":"day"})
        for i in days:
            date = i.find("h1", {"class":"heading"}).text # date format: "day-of-the-week, dd month yyyy"
            news_list = i.find("ul", {"class":"list"}).find_all("article")
            for news in news_list:
                news_time = news.find("li", {"class":["time", "large"]}).find("p").text # military time format
                news_category = news.find("p", {"class":"category"}).text[:-1]
                news_img_link = news.find("li", {"class":"image"}).find("img")['src']
                news_link = news.find("li", {"class":"image"}).find("a")["href"]
                news_headline = news.find("a", {"class":"title"}).text 
                news_description = news.find_all("p", {"class":"nohide"})[-1]
                list_of_news.append(self.NewsPage(self.base + news_link, headline = news_headline, description = news_description, img_link = news_img_link, date = date[-13:]))
        
        return list_of_news


    class NewsPage:
        def __init__(self, news_link, headline=None, description=None ,author=None, date=None, text=None, img_link=None, content_images=None, content_links=None, iframe = None, tags=None, categories=None):
            self.link = news_link
            self.headline = headline
            self.description = description
            self.author = author
            self.img_link = img_link
            self.date = date
            self.text = text
            self.content_images = content_images
            self.content_links = content_links
            self.iframe = None
            self.tags = tags
            self.categories = categories
            self.soup = None
        
        def __str__(self):
            return self.headline

        def page_soup(self):
            if not self.soup:
                page = requests.get(self.link)
                content = page.content
                soup = BeautifulSoup(content, 'html.parser')
                self.soup = soup
                return self.soup
            else:
                return self.soup
        

        def get_headline(self):
            if not self.headline:
                self.headline = self.page_soup().find(id="sectionHead").text
                return self.headline

        def get_description(self):
            if not self.description:
                self.description = self.page_soup().find("p", {"class":"intro"}).text
                return self.description

        def get_text(self):
            self.text = self.page_soup().find(id="news-item").text
            return self.text
        
        def get_author(self):
            details = self.page_soup().find(id="detail")
            self.author = details.find_all("li")[0].text.split("/")[1]
            return self.author

        def get_date(self):
            details = self.page_soup().find(id="detail")
            self.date = details.find_all("li")[1].text.split("/")[2:] # date format: ['dd Mon YYYY', 'H:MM Military']
            return self.date
        
        def get_categories(self):
            details = self.page_soup().find(id="detail")
            self.categories = [i for i in details.find_all("li")[2].text.split("/")[1:]]
            return self.categories
        
        def get_tags(self):
            self.tags = self.page_soup().find("div", {"class":"f16"}).text if self.page_soup().find("div", {"class":"f16"}) else " "
            return self.tags
        
        def get_img_link(self):
            if not self.img_link:
                self.img_link = self.page_soup().find(id="news-item").find("figure")['src']
                return self.img_link
        
        def get_content_images(self):
            if self.page_soup().find(id="news-item").find("img"):
                self.content_images = [i['src'] for i in self.page_soup().find(id="news-item").find_all("img")]
                return self.content_images
            else:
                None

        def get_content_links(self):
            if self.page_soup().find(id="news-item").find("a"):
                self.content_links = [i['href'] for i in self.page_soup().find(id="news-item").find_all("a") if i.has_attr('href')]
                return self.content_links
            else:
                None
        
        def get_iframe(self):
            if self.page_soup().find(id="news-item").find("iframe"):
                self.iframe = [i['src'] for i in self.page_soup().find(id="news-item").find_all("iframe")]
                return self.iframe

        def get_all(self):
            self.get_author()
            self.get_categories()
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

        def to_json():
            return json.dumps(self.__dict__)




