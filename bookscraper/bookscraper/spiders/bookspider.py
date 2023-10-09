import scrapy
import json


class BooksSpider(scrapy.Spider):
    name = 'books'
    

    def start_requests(self):
        self.my_dict = {}
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
        with open('my_dict.json', 'w') as f:
            json.dump(self.my_dict, f)

    def parse_products(self, response):
        pres = "https://www.techpowerup.com"
        for url in response.css('div.board-table-title__inner a::attr(href)').getall():
            print("url",url)
            yield scrapy.Request(pres+url, callback=self.pasre_Gpu,
                                 dont_filter=True)
    

    def pasre_Gpu(self, response):
        # print("GPU ",response.css('h1.gpudb-name::text').getall())
        gpuname = response.css('h1.gpudb-name::text').get()
        print("GPU ",gpuname)
        self.my_dict[gpuname] = {}
        self.my_dict[gpuname]["gpuname"] = gpuname
        sepcs =  response.css('dl.dl dt::text').getall()
        values = response.css('dl.dl dd::text').getall()
        for i in range(len(sepcs)):
            self.my_dict[gpuname][sepcs[i]] = values[i]
            # break
    

# mytag::text
