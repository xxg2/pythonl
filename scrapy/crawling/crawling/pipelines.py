# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
import csv
import itertools
reload(sys)
sys.setdefaultencoding('utf8')

class CrawlingPipeline(object):
    def process_item(self, item, spider):
        return item
