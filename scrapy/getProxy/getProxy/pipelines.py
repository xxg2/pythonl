# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GetproxyPipeline(object):
    def process_item(self, item, spider):
        fileName = 'proxy.txt'
        with open(fileName, 'a') as fp:
            fp.write(item['ip'].encode('utf8') + '\t')
            fp.write(item['port'].encode('utf8') + '\t')
            fp.write(item['type'].encode('utf8') + '\t')
            fp.write(item['location'].encode('utf8') + '\n')
        return item
