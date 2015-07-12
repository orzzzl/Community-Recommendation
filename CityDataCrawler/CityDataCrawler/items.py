# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CitydatacrawlerItem(scrapy.Item):
    zip = scrapy.Field()   #zip code
    zcpi2011 = scrapy.Field()    #zip code population in 2011: (include estimated ones)
    zcpi2010 = scrapy.Field()    #zip code population in 2010: (include estimated ones)
    zcpi2000 = scrapy.Field()    #zip code population in 2010: (include estimated ones)
    wp = scrapy.Field()    #White population
    bp = scrapy.Field()    #Black population
    aip = scrapy.Field()    #American Indian population
    ap = scrapy.Field()    #Asian population
    nhaopip = scrapy.Field()    #Native Hawaiian and Pacific Islander population
    sorp = scrapy.Field()    #Some other races population
    tomrp = scrapy.Field()    #two or more races population
    holp = scrapy.Field()    #Hispanic or Latino population
