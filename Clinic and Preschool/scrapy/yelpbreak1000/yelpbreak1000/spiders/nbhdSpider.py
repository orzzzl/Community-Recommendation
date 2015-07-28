import scrapy

class nbhdSpider (scrapy.Spider):
	name = "nbhd"
	doman = ["yelp.com"]
	start_urls = ["http://www.yelp.com/search?find_desc=day+care&find_loc=New+York%2C+NY&ns=1#start=0"]
	

	def parse (self, response):
		f = open ("/Users/April/PycharmProjects/yelpbreak1000/nbhds.json", "w")
		for sel in response.xpath ("//ul[@class='more place-more']/li"):
			temp = sel.xpath ("span/text()").extract()[0]
			# s = str (temp)
			# f.write (s)
			if temp == " Cities":
				continue
			else:
				for sel2 in sel.xpath (".//input"):
					temp2 = sel2.xpath("@value").extract()[0]
					f.write (temp2)
					f.write ("\n")
		f.close()

		# f = open ("/Users/April/PycharmProjects/yelpbreak1000/nbhditem.json", "w")
		# for sel in response.xpath("//ul[@class='more place-more']//input"):
		# 	temp = sel.xpath("./@value").extract()[0]
		# 	s = str (temp)
		# 	f.write (s)
		# 	f.write ("\n")
		# f.close()
			# item = Yelpbreak1000Item ()
			# item["name"] = sel.xpath("./@value").extract()[0]
			# yield item
