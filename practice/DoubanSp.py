import requests
import time
import random
import re
import json
from fake_useragent import UserAgent

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.i = 0

    def get_headers(self):
        headers = {'User-Agent': UserAgent().random}
        return headers
    
    def get_page(self,params):
        html = requests.get(url=self.url,params=params,headers=self.get_headers()).text
        html = json.loads(html)
        self.parse_page(html)

    def parse_page(self,html):
        item = {}
        for one in html:
            item['name'] = one['title'].strip()
            item['score'] = one['score'].strip()
            item['region'] = one['regions']
            item['type'] = one['types']
            item['actor'] = one['actors']
            print(item)
            self.i +=1
    
    def total_number(self,type_number):
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90&action='.format(type_number)
        headers = self.get_headers()
        html = requests.get(url=url,headers=headers).json()
        total = int(html['total'])
        return total

    def get_all_type_fimes(self):
        url = 'https://movie.douban.com/chart'
        headers = self.get_headers()
        html = requests.get(url=url,headers=headers).text
        re_bds = '<a href="/typerank\?type_name=(.*?)&type=(.*?)&interval.*?</a>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        type_dict = {}
        menu = ''
        for r in r_list:
            type_dict[r[0].strip()] = r[1].strip()
            menu += r[0].strip() + '|'
        return type_dict,menu
    
    def run(self):
        type_dict,menu = self.get_all_type_fimes()
        menu = menu + '/n电影类型: '
        name = input(menu)
        type_number = type_dict[name]
        total = self.total_number(type_number=type_number)
        for start in range(0,(total+1),20):
            params = {
                'type':type_number,
                'interval_id':'100:90',
                'action':'',
                'start':str(start),
                'limit':'20'
            }
            self.get_page(params=params)
            time.sleep(random.randint(1,3))
        print('该类型有电影{}部'.format(total),'/n获得信息{}部'.format(self.i))

if __name__=='__main__':
    spider = DoubanSpider()
    spider.run()

