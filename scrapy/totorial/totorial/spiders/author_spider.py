import scrapy

class AuthorSpider(scrapy.Spider):
    name = "author"
    start_urls = ['http://quotes.toscrape.com']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.css('.author + a::attr(href'):
            yield response.follow(href, self.parse_author)
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthday': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text')
        }