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
    males = scrapy.Field()    #Number of Males
    females = scrapy.Field()    #Number of Females
    hac = scrapy.Field()    #Houses and condos
    roa = scrapy.Field()    #Renter-occupied apartments
    coliizc = scrapy.Field()    #cost of living index in zip code
    la = scrapy.Field()    #Land area      sq. mi.
    wa = scrapy.Field()    #water area      sq. mi.
    pd = scrapy.Field()    #Population density     How many people per sq mile
    mreptpfhuwm = scrapy.Field()    #Median real estate property taxes paid for housing units with mortgages
    mreptpfhuwnm = scrapy.Field()    #Median real estate property taxes paid for housing units with no mortgage
    hsoh = scrapy.Field()    #High school or higher
    bdoh = scrapy.Field()    #Bachelor's degree or higher
    gopd = scrapy.Field()    #Graduate or professional degree
    unemployed = scrapy.Field()    #Unemployed
    mtttw = scrapy.Field()    #Mean travel time to work
    neverm = scrapy.Field()    #Never married
    nowm = scrapy.Field()    #Now married
    seperated = scrapy.Field()    #Separated
    widowed = scrapy.Field()    #Widowed
    divorced = scrapy.Field()    #Divorced
    mhv = scrapy.Field()    #Median house value
    rp = scrapy.Field()    #Renting percentage
    lossmi = scrapy.Field()    #Length of stay since moving in
    norph = scrapy.Field()    #Number of rooms per house
    nocs = scrapy.Field()    #Number of college students
    popwabdoh = scrapy.Field()    #Percentage of population with a bachelor's degree or higher
    lc = scrapy.Field()    #Lesbian couples
    gm = scrapy.Field()  #Gay men
    mmocfuwitham = scrapy.Field()    #Median monthly owner costs for units with a mortgage
    mmocfuwithoutam = scrapy.Field()    #Median monthly owner costs for units without a mortgage

