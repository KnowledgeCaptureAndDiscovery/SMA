# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PyLibSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lib_name =  scrapy.Field()
    lib_ver = scrapy.Field()
    lib_desc = scrapy.Field()
