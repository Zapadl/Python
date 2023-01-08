import requests
from bs4 import BeautifulSoup as bs
import numpy as np


URL_TEMPLATE = "https://mixnews.lv/yumor"
FILE_NAME = "test.txt"

def parse_url(url = URL_TEMPLATE):
    result_list = {'href': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    url_post = soup.find_all("div",class_="post-item-normal one-posts")
    for name in url_post:
        result_list['href'].append(name.a['href'])
    return result_list

def parse_post_title(url = URL_TEMPLATE):
    result_list = {'h4': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    post_title = soup.find_all("h4")
    for name in post_title:
        result_list['h4'].append(name.text)
    return result_list

# def parse_url(url = URL_TEMPLATE):
#     result_list = {'href': [][]}
#     r = requests.get(url)
#     soup = bs(r.text, "html.parser")
#     url_post = soup.find_all("div",class_="post-item-normal one-posts")
#     post_title = soup.find_all("h4")
#     for name in url_post:
#         result_list['href'].append(name.a['href'] )
#         result_list['href'].append(name.text)
#     return result_list

print(parse_url())
print(parse_post_title())




