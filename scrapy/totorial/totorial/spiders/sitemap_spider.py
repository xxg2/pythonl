# -*- coding: utf-8 -*-
import scrapy


class SitemapSpider(scrapy.Spider):
    name = 'sitemap_spider'
    allowed_domains = ['example.com']
    sitemap_urls = ['http://example.com/']
    sitemap_rules = [('/product/', 'parse_product'),
                     ('/category/', 'parse_category')]

    def parse_product(self, response):
        pass

    def parse_category(self, response):
        pass