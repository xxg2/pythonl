# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from totorial.items import TotorialItem

class CsvSpider(CSVFeedSpider):
    name = 'csv_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.csv']
    delimiter = ';'
    quotechar = "'"
    headers = ['id', 'name', 'description']

    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row!: %r', row)

        item = TotorialItem()
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item
