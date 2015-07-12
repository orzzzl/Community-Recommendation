# -*- coding: utf-8 -*-

# Scrapy settings for CityDataCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CityDataCrawler'

SPIDER_MODULES = ['CityDataCrawler.spiders']
NEWSPIDER_MODULE = 'CityDataCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CityDataCrawler (+http://www.yourdomain.com)'
