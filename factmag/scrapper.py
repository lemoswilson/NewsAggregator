import requests
from bs4 import BeautifulSoup
import json


# at first just collect data from the news after 2015..


class FactMagScrapper:
    def __init__(self):
        self.news_page = 'https://www.factmag.com/category/news/page/'
        self.tech_page = 'https://www.factmag.com/category/tech/page/'
    
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
        post_dict = {"link": info['href'], "title": info['title'], "image-link":img_link}




        post = requests.get(post_dict['link'])
        post_content = post.content
        soup_content = BeautifulSoup(post_content, "html.parser")

        divider = soup_content.find("span", {"class":"f-author"})
        date = divider.nextSibling.nextSibling.nextSibling.text
        post_dict['date'] = date # date format dd.mm.yy

        post_text = soup_content.find("div", {"class":"entry-content"})
        if post_text.find("a"):
            link_list = [i['href'] for i in post_text.find_all("a")]
            post_dict['content-links'] = link_list
        else:
            post_dict['content-links'] = None

        if post_text.find("img"):
            images = post_text.find_all("img")
            images_src = []
            for i in images:
                try:
                    images_src.append([i['src'], i['srcset']])
                except:
                    images_src.append(i['src'])
            post_dict['content-images'] = images_src
        else:
            post_dict['content-images'] = None
        
        p = post_text.find_all("p")
        p_content = str()
        for t in p:
            p_content += t.text
        
        tags = soup_content.find("div", {"class":"article-tags"})
        tag_list = [tag.text for tag in tags.find_all("a")]
        
        author = soup_content.find("a", {"class":"author"}).text
        
        if post_text.find("iframe"):
            iframe = post_text.find_all("iframe")
            iframe_src = [i['src'] for i in iframe]
            post_dict['iframe'] = iframe_src
        else:
            post_dict['iframe'] = None
        
        post_dict['tags'] = tag_list
        post_dict['content'] = p_content
        post_dict['author'] = author
        return post_dict


    def get_posts_info(self, category, p_number):
        post_info = {}
        if category == 'tech':
            base_link = self.tech_page
        elif category == 'news':
            base_link = self.news_page
        else:
            return "not valid category, choose between 'news' or 'tech'"
        
        posts_lists = []
        page = requests.get(base_link + str(p_number))
        page_content = page.content
        page_soup = BeautifulSoup(page_content, "html.parser")
        posts_div = page_soup.find_all("div", {"class":"block-post-wrapper"})
        for div in posts_div:
            to_post = div.find("a")
            post_meta = div.find('p', {'class':'meta'})
            img_srcs = [div.find("img")['src'], div.find("img")['srcset']]
            post_dict = {"link": to_post['href'], "title": to_post['title'], "date":post_meta.find_all("span")[1].text, "image-link":img_srcs}
            
            post = requests.get(post_dict['link'])
            post_content = post.content
            soup_content = BeautifulSoup(post_content, "html.parser")

            post_text = soup_content.find("div", {"class":"entry-content"})
            if post_text.find("a"):
                link_list = [i['href'] for i in post_text.find_all("a")]
                post_dict['content-links'] = link_list
            else:
                post_dict['content-links'] = None

            if post_text.find("img"):
                images = post_text.find_all("img")
                images_src = []
                for i in images:
                    try:
                        images_src.append([i['src'], i['srcset']])
                    except:
                        images_src.append(i['src'])
                post_dict['content-images'] = images_src
            else:
                post_dict['content-images'] = None
            
            p = post_text.find_all("p")
            p_content = str()
            for t in p:
                p_content += t.text
            
            tags = soup_content.find("div", {"class":"article-tags"})
            tag_list = [tag.text for tag in tags.find_all("a")]
            
            author = soup_content.find("a", {"class":"author"}).text
            
            if post_text.find("iframe"):
                iframe = post_text.find_all("iframe")
                iframe_src = [i['src'] for i in iframe]
                post_dict['iframe'] = iframe_src
            else:
                post_dict['iframe'] = None
            
            post_dict['tags'] = tag_list
            post_dict['content'] = p_content
            post_dict['author'] = author
            posts_lists.append(post_dict)
        return posts_lists

scrapper = FactMagScrapper()
# print(scrapper.get_posts_info('news', 1))
print(scrapper.get_highlight_post('tech'))

# title
# link
# author
# image-link
# date
# text
# content-images
# content-links
# iframe
# tags