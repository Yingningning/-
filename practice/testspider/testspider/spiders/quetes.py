import scrapy
from lxml import etree
from testspider.items import TestspiderItem


class QuetesSpider(scrapy.Spider):
    name = "quetes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):

        quotes = response.xpath('//div[@class="quote"]')
        for quote  in quotes:
            item = TestspiderItem()
            item['text'] = quote.xpath('./span[@class="text"]/text()')
            item['author'] = quote.xpath('./span/small/text()')
            tags = quote.xpath('./div[@class="tags"]//text()')
            item['tags'] = tags
            yield item
        nextpage = response.xpath('//li[@class="next"]/a/@href')[0].extract()
        url = response.urljoin(nextpage)
        yield scrapy.Request(url=url,callback=self.parse)