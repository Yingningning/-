import scrapy
from scrapy import Selector,Request
from douban250.items import Douban250Item

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]
    

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for list_item in list_items:
            movie_item = Douban250Item()
            movie_item['title']   = list_item.xpath('.//span[@class="title"]//text()').get()#get返回第一个，
            movie_item['rank']    = list_item.xpath('.//span[@class="rating_num"]/text()').get()
            movie_item['subject'] = list_item.xpath('.//span[@class="inq"]/text()').get()
            detail_url = list_item.xpath('.//div[@class="hd"]/a/@href').get()
            yield Request(url=detail_url,callback=self.parse_detail,cb_kwargs={'item':movie_item})

        url = sel.xpath('//span[@class="next"]/a/@href').get()
        url = response.urljoin(url) 
        print(url)
        yield Request(url=url,callback=self.parse)

    def parse_detail(self,response,**kwargs):
        movie_item = kwargs['item']
        sel = Selector(response)
        movie_item['duration'] = sel.xpath('//*[@id="info"]/span[@property="v:runtime"]/text()').get()
        movie_item['intro'] = ','.join(sel.xpath('//span[@class="all hidden"]/text() | //span[@property="v:summary"]/text()').getall()).strip()
        yield movie_item
        
