import scrapy
import json


class BooksSpider(scrapy.Spider):
    name = 'books'
    my_dict = {}
    with open('my_dict.json', 'w') as f:
        json.dump(my_dict, f)

    def start_requests(self):
        # url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
        url = 'https://www.techpowerup.com/gpu-specs/?mfgr=AMD&mobile=No&igp=No&sort=name'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # item = {}
        pres = "https://www.techpowerup.com"
        count = 0
        for url in response.css('td.vendor-AMD a::attr(href)').getall():
            print(pres+url)
            count += 1
            yield scrapy.Request(pres+url, callback=self.parse_products,
                                 dont_filter=True)
            if count > 4:
                break

    def parse_products(self, response):
        pres = "https://www.techpowerup.com"
        for url in response.css('div.board-table-title__inner a::attr(href)').getall():
            print("url",url)
            yield scrapy.Request(pres+url, callback=self.pasre_Gpu,
                                 dont_filter=True)
    

    def pasre_Gpu(self, response):
        print("GPU ",response.css('h1.gpudb-name::text').getall())
            # break

# mytag::text
