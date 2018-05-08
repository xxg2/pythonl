# -*- coding: utf-8 -*-
from totorial.items import TotorialItem


class ItemSpider(scrapy.Spider):
    name = 'item_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        product = TotorialItem(name='Desktop', price=1000)

        product['name']
        product.get('name')
        product['price']
        product['last_updated']
        product.get('last_updated', 'not set')
        product.get('lala', 'unknow field')

        'name' in product # True
        'last_updated' in product # False
        'last_updated' in product.fields # True

        product['last_updated'] = 'today'

        product.keys() # ['name','price']
        product.items() # [('price', 1000), ('name', 'Desktop')]

        product2 = TotorialItem(product)
        product3 = product2.copy()

        dict(product)  #{'price': 1000, 'name': 'Desktop'}

        TotorialItem({'price': 1000, 'name': 'Desktop'})
        pass
