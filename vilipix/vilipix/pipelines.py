# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class VilipixPipeline:
    def process_item(self, item, spider):
        return item

class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item):
        url = request.url
        file_name = item['name'] + '-' + url.split('/')[-1]
        return file_name        
    
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok,x in results]
        if not image_paths:
            raise DropItem('DOWNLOAD FAILED')
    
    def get_media_requests(self, item, info):
        yield Request(item['image_url'])