# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem

class ProxySpider(scrapy.Spider):
    name = 'proxySpider'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha']

    def parse(self, response):
        subSelector = response.xpath('//table/tbody/tr')
        items = []
        for sub in subSelector:
            item = GetproxyItem()
            item['ip'] = sub.xpath('./td//text()')[0].extract()
            item['port'] = sub.xpath('./td//text()')[1].extract()
            item['type'] = sub.xpath('./td//text()')[3].extract()
            item['location'] = sub.xpath('./td//text()')[4].extract()
            items.append(item)
        return items