import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quote"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        # if you run command scrapy crawl quotes -o quotes-humor.json -a tag=humor.
        # The tag=humor, url will be http://quotes.toscrape.com/tag/humor
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    # def parse(self, response):
    #     for quote in response.css('dev.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first()
    #         }
    #
    #     next_page = response.css('li.next a::attr(href)').extract_first()
    #     if next_page is not None:
    #         yield response.follow(next_page, self.parse)

    def parse(self, response):
        for h3 in response.xpath('//h3').extract():
            yield {"title": h3}

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)