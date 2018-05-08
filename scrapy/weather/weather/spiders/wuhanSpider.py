# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class WuhanspiderSpider(scrapy.Spider):
    name = 'wuHanSpider'
    allowed_domains = ['tianqi.com']
    start_urls = []
    cities = ['wuhan', 'shanghai']

    for city in cities:
        start_urls.append('http://'+city+'.tianqi.com/')

    def parse(self, response):
        subSelector = response.xpath('//dl[@class="weather_info"]')
        # for sub in subSelector:
        item = WeatherItem()
        # item['cityDate'] = subSelector.xpath('./dd[1]/h2//text()').extract()
        item['week'] = subSelector.xpath('./dd[2]//text()').extract()
        item['img'] = subSelector.xpath('./dd[3]/i/img/@src').extract()
        item['weather'] = subSelector.xpath('./dd[3]/i/img/@src').extract()
        item['wind'] = subSelector.xpath('./dd[4]/b[2]').extract()
        return item
