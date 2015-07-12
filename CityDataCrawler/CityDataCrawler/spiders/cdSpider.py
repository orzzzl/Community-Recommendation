__author__ = 'zelengzhuang'

import scrapy
from CityDataCrawler.items import CitydatacrawlerItem
from bs4 import BeautifulSoup as bs
from urlparse import urljoin as uj
import re
from time import sleep

class cdSpider (scrapy.Spider):
    name = 'cdSpider'
    allowed_domains = ["city-data.com"]
    start_urls = ['http://www.city-data.com/city/New-York-New-York.html']
    soup = None

    def parse (self, response):
        soup = bs (response.body, 'html.parser')
        urlDivs = soup.find(id='zip-codes').find('p').find_all('a')
        cnt = 0
        for url in urlDivs :
            target_url = uj("http://www.city-data.com/", url.get('href'))
            print "current processing url:  %s\n %d urls processed" % (target_url, cnt)
            cnt += 1
            sleep (1)
            yield scrapy.Request (target_url, callback=self.process)

    def process (self, response):
        self.soup = bs (response.body, 'html.parser')
        item = CitydatacrawlerItem ()
        item ['zip'] = response.url.split ('/') [-1] [0: 5]
        item ['zcpi2011'] = self.query ("[Zz]ip code population in 2011:")
        item ['zcpi2010'] = self.query ("[Zz]ip code population in 2010:")
        item ['zcpi2000'] = self.query ("[Zz]ip code population in 2000:")
        item ['wp'] = self.query ("White population:")
        item ['bp'] = self.query ("Black population:")
        item ['aip'] = self.query ("American Indian population:")
        item ['ap'] = self.query ("Asian population:")
        item ['nhaopip'] = self.query ("Native Hawaiian and Other Pacific Islander population:")
        item ['sorp'] = self.query ("Some other race population:")
        item ['tomrp'] = self.query ("Two or more races population:")
        item ['holp'] = self.query ("Hispanic or Latino population:")
        yield item

    def query (self, textContent) :
        attEle = self.soup.find(text=re.compile(textContent))
        if not attEle:
            return None
        itsParent = attEle.find_parent()
        return itsParent.next_sibling

