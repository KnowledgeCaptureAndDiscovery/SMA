import scrapy
from py_lib_spider import items

class PypiSpider(scrapy.Spider):
    name = 'pypi'
    allowed_domains = ['pypi.org']
    start_urls = ['https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3']

    def parse(self, response):

        lib_info = response.xpath("//a[@class='package-snippet']")
        for lib in lib_info:
            lib_dic = {}
            name = lib.xpath("./h3/span[@class='package-snippet__name']/text()").get()
            version = lib.xpath("./h3/span[@class='package-snippet__version']/text()").get()
            desc = lib.xpath("./p/text()").get()
            lib_dic[name] = {'version':version,'description':desc}
            yield lib_dic


        next_page= response.xpath("//a[contains(text(),'Next')]/@href").get()
        if next_page :
            yield response.follow(next_page,callback=self.parse)



