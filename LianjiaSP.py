import requests
import random
from lxml import etree
import time
import csv
from fake_useragent import UserAgent

class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg2/'
        self.blog = 1
    
    def get_header(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers
    
    def get_html(self,url):
        #在超时间内，对于失败页面尝试请求三次
        if self.blog <=3:
            try:
                res = requests.get(url=url,headers=self.get_header(),timeout=3,
                                   cookies={'Cookie':"select_city=110000; lianjia_ssid=9eea9c67-df0f-4189-8491-81aa1e8e9912; lianjia_uuid=d6172c2e-9253-4ca3-92d3-e193672adc3c; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1716880714; sajssdk_2015_cross_new_user=1; _smt_uid=6655854a.9ccc8d1; _ga=GA1.2.233535302.1716880716; _gid=GA1.2.234814442.1716880716; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218fbe10a931907-0e49a0dcf35d1b-4c657b58-3686400-18fbe10a9321390%22%2C%22%24device_id%22%3A%2218fbe10a931907-0e49a0dcf35d1b-4c657b58-3686400-18fbe10a9321390%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; login_ucid=2000000423250681; lianjia_token=2.0010b05f4441617851011d7675a710324c; lianjia_token_secure=2.0010b05f4441617851011d7675a710324c; security_ticket=A5yqXZaFdKkViEbH2yEtTwUtSoBj4IWTO/c/3CMCuhiezwd0CyIaNfUlF2NsbJ5+sQMozy5+VhRt+ZNnsXZHwcORifAs9IKRnnN7B+0m+k6o4F+0fPIcYX+M/UsRl87ekxNHsq15mCZx1Hw6RfbDZLYMXtLuic57bjPbF9kJMPg=; ftkrc_=7f7fa17f-1435-44dc-bd53-6454cb271eb1; lfrc_=71d6b307-8ce9-4346-82ec-a9dc70b7f735; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1716885853; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMjQwNGU0N2I1OWNkYmUzZWQ1ZWJhMGFkYWMwZmRlNzAyM2JkZDU4MzM2MzFlMGFmYzk5OTI1Yzc4MjI5YzhhOTAyNzVlMzgyODNiZTI4MmY3NTNlMGZiYWU2OGM4NWMwZGMzY2Y0OGJhOTNhM2IzNjEwYzY5MGRiY2Y2ZmZkNTcyNjQwOWZhYWE1ODZiYTNjNjUzYjViMDgxYjc4NTEzZTViY2M2ODJmNDk4NmFkNWRmMTQ3ZmM2OTNiODJkMmQxNDAwYjVlODBiZGFjMzA5ZDE0M2Q0ODIzODUyOWE2YjYxZWViNWM4ZTI4MmU4Yjc5NTYyYjYzYmYyMjA3OGE4M1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJjMzdiYzJmZFwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcGcyLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_KJTRWRHDL1=GS1.2.1716885577.2.1.1716885854.0.0.0; _ga_QJN1VP0CMS=GS1.2.1716885577.2.1.1716885854.0.0.0",
                                            'Cache-Control':"max-age=0"}
                                
                                )
                html = res.text
                return html
            except Exception as e:
                print(e)
                self.blog+=1
                self.get_html(url=url)
    
    def parse_html(self,html):
        if html:
            # with open('lianjia.txt','w',encoding='utf-8') as f:
            #     f.write(html)
            p = etree.HTML(html)
            items = []
            #基准表达式
            h_list = p.xpath("//div[@class='leftContent']/ul[@class='sellListContent']/li[@class='clear LOGVIEWDATA LOGCLICKDATA']")
            #所有列表价节点对象
            for h in h_list:
                item = {}
                name = h.xpath("./div[@class='info clear']/div[@class='title']/a/text()")
                item['name'] = name[0] if name else None
                address = h.xpath("./div[@class='info clear']/div[@class='flood']/div[@class='positionInfo']/text()")
                item['address'] = address[0].strip()
                info = h.xpath("./div[@class='info clear']/div[@class='address']/div[@class='houseInfo']/text()")
                if info:
                    L = info[0].split('|')
                    item['model'] = L[0].strip()
                    item['area'] = L[1].strip()
                    item['direction'] = L[2].strip()
                    item['show'] = L[3].strip()
                    item['floor'] = L[4].strip()
                    if len(L) >=7:
                        item['time'] = L[5].strip()
                        item['type'] = L[6].strip()
                    else:
                        item['time'] = None
                        item['type'] = L[5].strip()
                total_price = h.xpath("./div[@class='info clear']/div[@class='priceInfo']/div[@class='unitPrice']/span/text()")
                sum_price = h.xpath("./div[@class='info clear']/div[@class='priceInfo']/div[@class='totalPrice totalPrice2']/span/text()")
                item['total_price'] = total_price[0].strip()
                item['sum_price'] = sum_price[0].strip() + '万'
                print(item)
                items.append(item)
            self.save_data(items)

    def save_data(self,items):
        with open('Lianjia.csv','a',newline='',encoding='utf-8') as f:
            writer = csv.DictWriter(f,fieldnames=items[0].keys())
            writer.writeheader()
            for item in items:
                writer.writerow(item)
    
    def run(self):
        try:
            html = self.get_html(self.url)
            self.parse_html(html=html)
        except Exception as e:
            print('erro{}'.format(e))

if __name__=='__main__':
    spider = LianjiaSpider()
    spider.run()

