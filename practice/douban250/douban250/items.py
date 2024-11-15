# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()
    duration = scrapy.Field()
    intro = scrapy.Field()
