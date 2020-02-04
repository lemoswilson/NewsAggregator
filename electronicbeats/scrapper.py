import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

class ElectronicBeats:
    def __init__(self):
        self.news_link = "https://www.electronicbeats.net/the-feed/"
        self.post_url = "https://www.electronicbeats.net/wp-admin/admin-ajax.php"

    class NewsPage:
        def __init__(self, link, )

    def get_news(number_of_pages):
        data = {
            "action": "LoadMoreFeeds",
            "paged": "2",
            "posts_per_page":"5"
        }
        request = requests.post(self.post_url, data)
        content = request.content
        sopa = BeautifulSoup(content, "html.parser")
        articles = sopa.find_all("li", {"class":"FeedOverview__Feed"})
        for i in articles:


# analyse the post response