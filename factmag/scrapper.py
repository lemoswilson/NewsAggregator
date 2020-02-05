import requests
from bs4 import BeautifulSoup
import json


# at first just collect data from the news after 2015..


class FactMagScrapper:
    def __init__(self):
        self.news_page = 'https://www.factmag.com/category/news/page/'
        self.tech_page = 'https://www.factmag.com/category/tech/page/'
    
    class NewsPage:
        def __init__(self, link, headline=None, author=None, date=None, text=None, img_link=None, content_images=None, content_links = None, iframe = None, tags=None, category=None):
            self.link = link
            self.headline = headline
            self.author = author
            self.date = date
            self.text = text
            self.img_link = img_link
            self.content_images = content_images
            self.content_links = content_links
            self.iframe = iframe
            self.tags = tags
            self.category = category
            self.soup = None

        def __str__(self):
            return self.headline

        def page_soup(self):
            if not self.soup:
                page = requests.get(self.link)
                content = page.content
                self.soup = BeautifulSoup(content, "html.parser")
            return self.soup

        def get_text(self):
            post_text = self.page_soup().find("div", {"class":"entry-content"})
            p = post_text.find_all("p")
            p_content = str()
            for t in p:
                p_content += t.text
            self.text = p_content
            return self.text
        
        def get_tags(self):
            tags = self.page_soup().find("div", {"class":"article-tags"})
            self.tags = [tag.text for tag in tags.find_all("a")]
            return self.tags
        
        def get_author(self):
            self.author = self.page_soup().find("a", {"class":"author"}).text
            return self.author

        def get_iframe(self):
            post_text = self.page_soup().find("div", {"class":"entry-content"})
            if post_text.find("iframe"):
                iframe = post_text.find_all("iframe")
                iframe_src = [i['src'] for i in iframe]
                self.iframe = iframe_src
            return self.iframe


        def get_content_images(self):
            post_text = self.page_soup().find("div", {"class":"entry-content"})
            if post_text.find("img"):
                images = post_text.find_all("img")
                images_src = []
                for i in images:
                    try:
                        images_src.append([i['src'], i['srcset']])
                    except:
                        images_src.append(i['src'])
                self.content_images = images_src
            return self.content_images
        
        def get_content_links(self):
            post_text = self.page_soup().find("div", {"class":"entry-content"})
            if post_text.find("a"):
                self.content_links = [i['href'] for i in post_text.find_all("a") if i.has_attr("href")]
            return self.content_links

        def get_date(self):
            divider = self.page_soup().find("span", {"class":"f-author"})
            date = divider.nextSibling.nextSibling.nextSibling.text
            self.date = date
            return self.date

        def get_all(self):
            self.get_author()
            self.get_content_images()
            self.get_content_links()
            self.get_date()
            self.get_iframe()
            self.get_tags()
            self.get_text()
            return self


    def get_highlight_post(self, category):
        if category == 'tech':
            base_link = self.tech_page
        elif category == 'news':
            base_link = self.news_page
        else:
            return "not valid category, choose between 'news' or 'tech'"
        
        page= requests.get(base_link + str(1))
        page_content = page.content
        page_soup = BeautifulSoup(page_content, "html.parser")
        post_div = page_soup.find("div", {"class":"spaces-post-content"})
        heading = post_div.find("h2")
        info = heading.find("a")
        image = page_soup.find("div", {"class":"spaces-featured-post"})["style"]
        img_link = image.split("url(")[1]
        img_link = img_link[:-1]
        return self.NewsPage(info['href'], headline = info['title'], img_link=img_link, category=category)


    def get_posts(self, category, p_number):
        if category == 'tech':
            base_link = self.tech_page
        elif category == 'news':
            base_link = self.news_page
        else:
            return "not valid category, choose between 'news' or 'tech'"
        
        posts_list = []
        page = requests.get(base_link + str(p_number))
        page_content = page.content
        page_soup = BeautifulSoup(page_content, "html.parser")
        posts_div = page_soup.find_all("div", {"class":"block-post-wrapper"})
        for div in posts_div:
            to_post = div.find("a")
            post_meta = div.find('p', {'class':'meta'})
            img_srcs = [div.find("img")['src'], div.find("img")['srcset']]
            posts_list.append(self.NewsPage(to_post['href'], headline=to_post['title'], date=post_meta.find_all("span")[1].text, img_link=img_srcs, category=category))

        return posts_list


scrapper = FactMagScrapper()
highlight_news = scrapper.get_highlight_post('news')
highlight_news.get_all()
print(highlight_news.author)
