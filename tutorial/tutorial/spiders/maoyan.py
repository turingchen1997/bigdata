# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
import time
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4/']
    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
}
    def parse(self, response):
        dl = response.css('.board-wrapper dd')
        for dd in dl:
            item = TutorialItem()
            item['index'] = dd.css('.board-index::text').extract_first()
            item['title'] = dd.css('.name a::text').extract_first()
            item['star'] = dd.css('.star::text').extract_first()
            item['releasetime'] = dd.css('.releasetime::text').extract_first()
            item['score'] = dd.css('.integer::text').extract_first() + dd.css('.fraction::text').extract_first()
            yield item
       
