# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class SelectorSpider(scrapy.Spider):
    name = 'selector_spider'
    allowed_domains = ['example.com']
    start_urls = ['https://doc.scrapy.org/en/latest/_static/selectors-sample1.html']

    def parse(self, response):
        #body = '<html><body><span>good</span></body></html>'
        #Selector(text = body).xpath('//span/text()').extract()

        #response = HtmlResponse(url='http://example.com', body=body)
        #Selector(response=response).xpath('//span/text()').extract()

        #response.selector.xpath('//span/text()').extract()

        # <html>
        #     <head>
        #         <base href='http://example.com/' />
        #         <title>Example website</title>
        #     </head>
        #     <body>
        #         <div id='images'>
        #             <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
        #             <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
        #             <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
        #             <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
        #             <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
        #         </div>
        #     </body>
        # </html>
        response.xpath('//title/text()') #response.css('title:text')
        response.css('img').xpath('@src').extract()
        response.xpath('//title/text()').extract()
        response.xpath('//div[@id="images"]/a/text()').extract_first()
        response.xpath('//div[@id="not_exist"]/a/text()').extract_first()  #return None
        response.xpath('//div[@id="not-exist"]/text()').extract_first(default='not-found') # return 'not-found'
        response.xpath('//base/@href').extract()        #response.css('base::attr(href)').extract()
        response.xpath('a[contains(@href, "image")]/@href').extract()
        response.css('a[href*=image]::attr(href)').extract()
        response.xpath('//a[contains(@href, "image")]/img/@src')
        response.css('a[href*=image] img::attr(src)').extract()
        response.xpath('//a[contains(@href, "image")]/text()').re('Name:\s*(.*)') #used to extract image names
        response.xpath('//div[@id=$val]/a/text()', val='images').extract_first()
        response.xpath('//div[count(a)=$cnt]/@id', cnt=5).extract_first()
        response.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()

        sel = Selector(text='<a href="#">Click here to go to the <strong>Next Page</strong></a>')
        sel.xpath('//a[1]').extract()
        sel.xpath('//a[contains(.//text(), "Next Page")]').extract()
        pass
