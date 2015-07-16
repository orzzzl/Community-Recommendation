import scrapy
from shopping.items import ShoppingItem
from urlparse import urljoin

class shoppingspider (scrapy.Spider):
	name = 'shoppingspider'
	allowed_domains = ["yelp.com"]
	url_base = "http://www.yelp.com/search?find_desc=Shopping&find_loc=New+York%2C+NY&start="
	page_index = 0
	start_urls = []
	while page_index < 1000:
		temp = '%d' % page_index
		target_url = url_base + temp
		page_index += 10
		start_urls.append(target_url)

	def parse(self, response):
		print "processing url:"
		print response.url
		selectors = response.xpath ('//li[@class="regular-search-result"]')
		for selector in selectors:
			item = ShoppingItem()
			name = selector.xpath ('descendant::a[@class="biz-name"]/text()').extract()
			addressresponse = selector.xpath('normalize-space(descendant::address)').extract()
			rating = selector.xpath('descendant::div[@class="rating-large"]/i/@title').extract()
			price = selector.xpath('descendant::span[@class="business-attribute price-range"]/text()').extract()
			item['name'] = name
			item['address'] = addressresponse
			item['rating'] = rating
			item['price'] = price
			yield item