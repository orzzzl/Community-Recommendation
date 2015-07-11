import scrapy
from sherlore.items import SherloreItem
from urlparse import urljoin 
from Queue import Queue

class sherloreSpider (scrapy.Spider):
    name = 'sherloreSpider'
    allowed_domains = ["sherlore.com"]
    start_urls = ["http://www.sherlore.com"]
    visited_urls = []
    q = Queue ()     

    def parse (self, response):
        self.q.put (response)
        while not self.q.empty ():
            current_response = self.q.get ()
            select = current_response.xpath ('//a')
            urls = []
            titles = []
            for sel in select:
                urls.append (urljoin (self.start_urls [0], sel.xpath ('@href').extract () [0]))
                titles.append (sel.xpath('text()').extract() [0])
            lenth = len (urls)
            for i in xrange (lenth):
                url = urls [i]
                title = titles [i]
                if url in self.visited_urls:
                    continue
                self.visited_urls.append (url)
                item = SherloreItem ()
                item ['title'] = title
                item ['url'] = url
                yield item
                yield scrapy.Request (urls [lenth - i - 1], callback = self.parse)

