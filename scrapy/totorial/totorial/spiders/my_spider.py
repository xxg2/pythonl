# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/']

    rules=(
        Rule(LinkExtractor(allow=('category\.php'), deny=('subsection\.php'))),
        Rule(LinkExtractor(allow=('item\.php'), deny=('parse_item')))
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['d'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
