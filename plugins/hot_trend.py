from selenium import webdriver
from plugins.utils import extract_from_tag
import json

def get_data():
    browser = webdriver.Chrome()
    browser.get(r'https://api.bilibili.com/x/web-interface/wbi/search/square?limit=10')

    res = extract_from_tag(browser.page_source, '<pre>')
    browser.close()
    data = json.loads(res[0])
    trending_list = data['data']['trending']['list']
    return_str = ""
    for item in trending_list:
        keyword = item['keyword']
        heat_score = item['heat_score']
        i = f"{keyword}" + "\n"
        return_str += i
    return return_str



