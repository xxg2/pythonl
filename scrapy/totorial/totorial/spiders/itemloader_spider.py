# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from totorial.items import TotorialItem

class ItemloaderSpider(scrapy.Spider):
    name = 'itemloader_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        l = ItemLoader(item=TotorialItem(), response=response)
        l.add_xpath('name', '//div[@class="product_name"]')
        l.add_xpath('name', '//div[@class="product_title"]')
        l.add_xpath('price', '//div[@id="price"]')
        l.add_css('stock', 'p#stock"]')
        l.add_value('last_udpated', 'today')
        return l.load_item()
