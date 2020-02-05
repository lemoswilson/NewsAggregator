import requests
from bs4 import BeautifulSoup  
from datetime import datetime
import json


class Pitchfork:
    def __init__(self):
        self.base = "https://pitchfork.com/news/?genre=electronic&page="

    def get_news(page_number):
        url = self.base + page_number


    class NewsPage:
        def __init__(self, link, )

# divided in three sections 
# 1 - <section class = "hero"
# 2 - <div class = "container-fluid"
# 3 - <div class= "lower-section"