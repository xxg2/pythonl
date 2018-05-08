# -*- coding: utf-8 -*-
import scrapy
from crawling.items import CrawlingItem
import re

class OrganizationSpider(scrapy.Spider):
    name = 'organizationSCSpider'
    allowed_domains = ['gzhfda.gov.cn']
    start_urls = ['http://www.gzhfda.gov.cn/search_searchshow_lx_spscnew_p_1_']
    page_num = 1

    def parse(self, response):
        orgTable = response.xpath('//table[@class="dataTable"]/tr')
        index = 1
        for sub in range(1, len(orgTable)):
            item = CrawlingItem()
            item['id'] = '%d_%d' % (self.page_num, index)
            item['name'] = orgTable[sub].xpath('./td[1]/a//text()').extract()
            item['code'] = orgTable[sub].xpath('./td[2]//text()').extract()
            item['cerType'] = 'SC'
            item['type'] = orgTable[sub].xpath('./td[3]//text()').extract()
            index = index + 1
            yield item
        self.page_num = self.page_num + 1
        if len(orgTable) == 21:
            next_page_url = 'http://www.gzhfda.gov.cn/search_searchshow_lx_spscnew_p_%d_' % self.page_num
            yield scrapy.Request(response.urljoin(next_page_url))
