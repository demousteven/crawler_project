# bbc_spider.py
import scrapy
from readability import Document
from items import NewsItem

class BBCSpider(scrapy.Spider):
    name = "bbc"
    start_urls = ['http://www.bbc.com/']

    def parse(self, response):
        for article_url in response.css('a.gs-c-promo-heading::attr(href)').extract():
            yield scrapy.Request(response.urljoin(article_url), callback=self.parse_article)

    def parse_article(self, response):
        doc = Document(response.text)
        item = NewsItem()
        item['url'] = response.url
        item['headline'] = doc.title()
        item['content'] = doc.summary()
        item['author'] = response.css('span.byline__name::text').get()
        yield item
