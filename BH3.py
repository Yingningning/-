import requests
from lxml import etree
import json
import time
import random
import os
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class BH3Spider(object):
    def __init__(self):
        self.url = 'https://api-takumi-static.mihoyo.com/content_v2_user/app/b9d5f96cd69047eb/getContentList?iPageSize=7&iPage={}&sLangKey=zh-cn&iChanId=699&isPreview=0'
        self.urls = {}
    def get_header(self):
        headers = {'User-Agent':UserAgent().random}
        return headers

    def get_pic_url(self,url):
        html = requests.get(url=url,headers=self.get_header()).text
        html = json.loads(html)
        lists = html['data']['list']
        for one in lists:
            sext = one['sExt']
            sext = json.loads(sext)
            key = sext.keys()
            infor = sext[list(key)[0]]
            url = infor[0]['url']
            name = sext[list(key)[1]]
            self.urls[name] = url
        time.sleep(random.randint(1,2))
    
    def get_pic(self):
        names = list(self.urls.keys())
        for name in names:
            url = self.urls[name]
            html = requests.get(url=url,headers=self.get_header()).content
            with open('./bh3/{}.png'.format(name),'wb') as f:
                f.write(html)
            print('{}下载成功'.format(name))
            time.sleep(random.randint(1,2))
    
    def run(self):
        for i in range(1,13):
            url = self.url.format(i)
            self.get_pic_url(url)
        urls = json.dumps(self.urls)
        directory = './bh3'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open('./bh3/pics_urls.txt','+a') as f:
            f.write(urls)
        self.get_pic()

if __name__=='__main__':
    BH3Spider().run()
