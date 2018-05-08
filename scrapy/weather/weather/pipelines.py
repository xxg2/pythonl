# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path
import urllib2
import json

class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        # fileName = today + '.txt'
        fileName = today+'.json'
        with open(fileName, 'a') as fp:
            # imgName = os.path.basename(item['img'])
            # fp.write(imgName+'\t')
            # if os.path.exists(imgName):
            #     pass
            # else:
            #     with open(imgName, 'w') as fp:
            #         response = urllib2.urlopen(item['img'])
            #         fp.write(response.read())
            # fp.write('%s\t' % item['week'][0].encode('utf8'))
            # fp.write('%s\t' % item['weather'][0].encode('utf8'))
            # fp.write('%s\n\n' % item['wind'][0].encode('utf8'))
            # time.sleep(1)
            line = json.dumps(dict(item), ensure_ascii=False)
            fp.write(line)
        return item
