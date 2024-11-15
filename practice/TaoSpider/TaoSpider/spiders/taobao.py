import scrapy
from scrapy import Request,Selector
from TaoSpider.items import TaospiderItem

class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["www.taobao.com"]
    item = TaospiderItem()

    def start_requests(self):
        tag = input('搜索物品：')
        page = int(input('搜索页数，一页48个： '))
        for i in range(page):
            url = 'https://s.taobao.com/search?page={}&q={}&tab=all'.format(i,tag)
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        item = TaospiderItem()
        goods = sel.xpath('//div[@class="Content--contentInner--QVTcU0M"]/div')
        for good in goods:
            item['title'] = good.xpath('.//div[@class="Title--title--jCOPvpf "]/span/text()').get()
            item['price'] = good.xpath('.//div[@style="margin-right: 8px;"]/text()').get()
            item['deal_count'] = good.xpath('.//span[@class="Price--realSales--FhTZc7U"]/text()').get()
            item['shop'] = good.xpath('.//a[@class="ShopInfo--shopName--rg6mGmy"]/text()').get()
            item['link'] = good.xpath('.//a[@class="Card--doubleCardWrapper--L2XFE73"]/@href').get()
            yield item