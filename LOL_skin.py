from fake_useragent import UserAgent
import requests
from lxml import etree
from bs4 import BeautifulSoup
import time
import os
import re
import json
import random

class LOL_skin(object):
    def __init__(self):
        self.url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2862761'
        self.path = './LOL_sink/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)
    def get_headers(self):
        headers = {
            'User-Agent':UserAgent().random,
        }
        return headers
    
    def get_heroid(self):
        path = self.path + 'heroid_url.txt'
        if not os.path.exists(path):
            headers = self.get_headers()
            html = requests.get(url=self.url,headers=headers).text
            html = json.loads(html)
            inf = {}
            hero_list = html['hero']
            for hero in hero_list:
                name = hero['name'] + '-' + hero['alias'] + '-' + hero['title']
                hero_id = hero['heroId']
                hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2862737'.format(str(hero_id))
                inf[name] = hero_url
            inf = json.dumps(inf)
            with open(path,'+w',encoding='utf-8') as f:
                f.write(inf)
            print('hero_urls get done')
        else:
            print('hero_urls exists')

    def get_sink(self):
        if os.path.exists('./LOL_sink/heroid_url.txt'):
            with open(self.path + 'heroid_url.txt','r',encoding='utf-8') as f:
                hero_urls = json.load(f)
        else:
            print('get urls error')
        for hero_name,url in hero_urls.items():
            html = self.get_imgurl(url=url)
            skins = html['skins']
            for skin in skins:
                skin_url = skin['mainImg']
                skin_name = skin['name']
                if skin_url:
                    self.get_img(url=skin_url,name=skin_name,dirname=hero_name)

    def get_imgurl(self,url):
        try:
            headers = self.get_headers()
            html = requests.get(url=url,headers=headers).text
            html = json.loads(html)
            return html
        except:
            print('RE-------get_imgurl')
            self.get_imgurl

    def get_img(self,url,dirname,name):
        if name[-1] == '"':
            name = name.replace('"','')
        if '/' or '\\' or '"' or ':' in name:
            name = name.replace('/','').replace('\\','').replace(':',' ')
        dirpath = self.path + '{}/'.format(dirname)
        picpath = dirpath + '{}.png'.format(name)
        if os.path.exists(picpath):
            print('{} pre-existing'.format(name))
        else:
            try:
                headers = self.get_headers()
                html = requests.get(url=url,headers=headers).content
                if not os.path.exists(dirpath):
                    os.makedirs(dirpath)
                with open(picpath,'wb') as f:
                    f.write(html)
                print('{}save done'.format(name))
                time.sleep(random.randint(1,2))
            except:
                print('RE-------get_img')
                self.get_img()

    def run(self):
        self.get_heroid()
        self.get_sink()

if __name__=="__main__":
    spider = LOL_skin()
    spider.run()






