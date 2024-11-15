from typing import Iterable
import scrapy
import re
from scrapy import Selector,Request
from vilipix.items import VilipixItem

from vilipix.spiders.utils import decode_specific_parts

class VilipixPicSpider(scrapy.Spider):
    name = "vilipix_pic"
    allowed_domains = ["www.vilipix.com"]
    
    def start_requests(self):
        for i in range(1,35):
            url = 'https://www.vilipix.com/tags/%E5%88%9D%E9%9F%B3/illusts?p={}'.format(i)
            yield Request(url=url,callback=self.parse_id)

    def parse_id(self,response):
        sel = Selector(response=response)
        pic_items = sel.xpath('//ul[@class="illust-content"]/li')
        for pic_item in pic_items:
            pic_url = pic_item.xpath('./div[@class="illust"]/a/@href').get()
            full_pic_url = response.urljoin(pic_url)
            yield Request(url=full_pic_url,callback=self.parse)

    def parse(self, response):
        item = VilipixItem()
        sel = Selector(response)
        name = sel.xpath('//div[@class="content"]/h2/text()').get()
        script = sel.xpath('//body/script[1]/text()').get()
        # print(script)
        pattern = re.compile(r'http:[^\s,;]*?origin[^\s,;]*?\.(?:png|jpg|PNG|JPG)')
        image_urls = re.findall(pattern=pattern,string=script)
        # print(image_urls)
        for image_url in image_urls:
            item['image_url'] = decode_specific_parts(image_url)
            item['name'] = name
            yield item

 