import scrapy
from yelpbreak1000.items import Yelpbreak1000Item
from urlparse import urljoin

class TxtSpider (scrapy.Spider):
    name = "text"
    f = open ("/Users/April/PycharmProjects/yelpbreak1000/nextpagetest.txt", "w")
    allowed_domains = ["yelp.com"]
    base = ["http://www.yelp.com"]
    # start_urls = ["http://www.yelp.com/search?find_desc=clinic&find_loc=New+York%2C+NY&ns=1&start=0&l=p:NY:New_York:Manhattan:Chelsea",
        # "http://www.yelp.com/search?find_desc=clinic&find_loc=New+York%2C+NY&ns=1&start=0&l=p:NY:New_York:Manhattan:Chinatown"]

    def get_start_urls ():
        urls = []
        foo = open ("/Users/April/PycharmProjects/yelpbreak1000/bronx.json")
        lines = foo.readlines ()
        for line in lines:
            url = "http://www.yelp.com/search?find_desc=preschool&find_loc=New+York%2C+NY&ns=1&start=0&l=p:" + line
            urls.append (url)
        foo.close ()
        return urls

    start_urls = get_start_urls ()

    def parse (self, response):
        temps = []
        for sel in response.xpath ("//li[@class='regular-search-result']"):
            item = Yelpbreak1000Item()

            temps.extend (sel.xpath (".//span[@class='indexed-biz-name']/a"))
            if len (temps) > 0:
                item["title"] = temps[0].xpath("text()").extract ()
            else:
                continue
            del temps[:]

            temps.extend (sel.xpath (".//span[@class='neighborhood-str-list']"))
            if len (temps) > 0:
                item["neighborhood"] = temps[0].xpath("text()").extract ()[0]
            else:
                item["neighborhood"] = "null"
            del temps[:]

            temps.extend (sel.xpath (".//address"))
            if len (temps) > 0:
                item["address"] = temps[0].xpath("text()").extract ()
            else:
                continue
            del temps[:]

            temps.extend (sel.xpath (".//span[@class='biz-phone']"))
            if len (temps) > 0:
                item["phoneNo"] = temps[0].xpath("text()").extract ()[0]
            else:
                item["phoneNo"] = "0"
            del temps[:]

            temps.extend (sel.xpath (".//div[@class='rating-large']/i"))
            if len (temps) > 0:
                item["rating"] = temps[0].xpath("@title").extract ()[0]
            else:
                item["rating"] = "0"
            del temps[:]

            temps.extend (sel.xpath (".//span[@class='review-count rating-qualifier']"))
            if len (temps) > 0:
                item["NoOfReview"] = temps[0].xpath("text()").extract ()[0]
            else:
                item["NoOfReview"] = "0"
            del temps[:]

            temps.extend (sel.xpath (".//span[@class='category-str-list']"))
            if len (temps) > 0:
                item["category"] = temps[0].xpath("a/text()").extract ()
            else:
                item["category"] = ["null"]
            del temps[:]
            self.f.write (str (item ['title']) + "\n")
            yield item

        nextpages = response.xpath ("//a[@class='page-option prev-next next']/@href").extract ()
        # length = len (nextpages)
        # s = str (length)
        # f.write (s)
        for nextpage in nextpages:
            url = urljoin (self.base[0], nextpage)
            yield scrapy.Request (url, callback = self.parse)
        #     f.write (url)
        #     f.write ('/n')

        # f.close ()
            

