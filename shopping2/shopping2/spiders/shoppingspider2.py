import scrapy
from shopping2.items import Shopping2Item
from urlparse import urljoin

class shoppingspider2 (scrapy.Spider):
	name = 'shoppingspider2'
	allowed_domains = ["yelp.com"]
	url_base1 = "http://www.yelp.com/search?find_desc=Shopping&find_loc=New+York%2C+NY&ns=1&start="
	page_index = 0
	start_urls = []

	NYCities = ["Manhattan", "Brooklyn", "Bronx", "Queens", "Staten_Island"]
	basePath1 = "./AreaData/"
	basePath2 = "Area.txt"

	for i in range(5):
		path = basePath1 + NYCities[i] + basePath2
		f = open(path, "r")
		while True:
			line = f.readline()
			if line:
				area = line.strip()
				urlAreaPart = "&l=p:NY:New_York:" + NYCities[i] + ":" + area
				for page_index in range(0, 1000, 10):
					tempStr = '%d' % page_index
					target_url = url_base1 + tempStr + urlAreaPart
					start_urls.append(target_url)
			else:
				break;
		f.close()

	def parse(self, response):
		print "processing url:"
		print response.url
		selectors = response.xpath ('//li[@class="regular-search-result"]')
		for selector in selectors:
			item = Shopping2Item()
			name = selector.xpath ('descendant::a[@class="biz-name"]/text()').extract()[0]
			addressresponse = selector.xpath('normalize-space(descendant::address)').extract()[0]
			if(selector.xpath('descendant::div[@class="rating-large"]/i/@title')):
				rating = selector.xpath('descendant::div[@class="rating-large"]/i/@title').extract()[0]
			else:
				rating = 'NONE'
			if(selector.xpath('descendant::span[@class="business-attribute price-range"]/text()')):
				price = selector.xpath('descendant::span[@class="business-attribute price-range"]/text()').extract()[0]
			else:
				price = 'NONE'
			item['name'] = name
			item['address'] = addressresponse
			item['rating'] = rating
			item['price'] = price
			yield item