# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoppingItem(scrapy.Item):
    name = scrapy.Field()
    rating = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()