# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Yelpbreak1000Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    neighborhood = scrapy.Field()
    address = scrapy.Field()
    phoneNo = scrapy.Field()
    rating = scrapy.Field()
    NoOfReview = scrapy.Field()
    category = scrapy.Field()
    pass

# class ClinicItem(scrapy.Item):
# 	title = scrapy.Field()
# 	neighborhood = scrapy.Field()
# 	address = scrapy.Field()
# 	phoneNo = scrapy.Field()
# 	rating = scrapy.Field()
# 	NoOfReview = scrapy.Field()
# 	category = scrapy.Field()
# 	pass