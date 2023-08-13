# items.py
import scrapy

class NewsItem(scrapy.Item):
    url = scrapy.Field()
    headline = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
