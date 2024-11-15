from urllib import request
import re
import time
import random
import csv
from fake_useragent import UserAgent

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/7'
    
    def get_html(self,url):
        headers = {'User-Agent':UserAgent().chrome,
                   'cookie':'__mta=208959789.1535106920033.1598509077842.1593509107607.47; _lxsdk_cuid=1710fbc224bc8-0048503dcb84eb-f313f6d-1a298c-1710fbc224cc8; mojo-uuid=bc73035186bc203e1e0a1a9d69cf0c8f; uuid_n_v=v1; uuid=010A4750BAB111EA977B252D9527D646FCA82B59C6B54FB3934C361D719643F2; _csrf=ab7e60b187089a5c797755f042abdbd14eed1760f8308dc455570ee9ea4edfa2; mojo-session-'}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(url=req)
        html = res.read().decode()
        self.parse_html(html)

    def parse_html(self,html):
        re_bds = '<div class="movie-item-info".*?<p class="name">.*?movieId:.*?>(.*?)<.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>'
        #生成正则表达式对象
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)

    def save_html(self,r_list):
        with open('maoyan.csv','a',newline='',encoding='utf-8') as f:
            #生成csv操作对象
            writer = csv.writer(f)
            #整理数据
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                time = r[2].strip()[5:]
                L = [name,star,time]
                writer.writerow(L)
                print(name,time,star)
    def run(self):
        self.get_html(self.url)
        time.sleep(random.randint(1,2))

if __name__=='__main__':
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print('错误：',e)

