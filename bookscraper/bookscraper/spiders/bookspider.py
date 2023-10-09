import scrapy
import json
import time

class BooksSpider(scrapy.Spider):
    name = 'books'
    my_dict = {}

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
            # if count > 3:
            #     break
            time.sleep(16)
        

    def parse_products(self, response):
        pres = "https://www.techpowerup.com"
        for url in response.css('div.board-table-title__inner a::attr(href)').getall():
            print("url",url)
            yield scrapy.Request(pres+url, callback=self.pasre_Gpu,
                                 dont_filter=True)
            time.sleep(8)
            # print("my_dict:",self.my_dict)

    def pasre_Gpu(self, response):
        # print("GPU ",response.css('h1.gpudb-name::text').getall())
        gpuname = response.css('h1.gpudb-name::text').get()
        print("GPU ",gpuname)
        self.my_dict[gpuname] = {}
        self.my_dict[gpuname]["gpuname"] = gpuname
        sepcs_values =  response.css('dl.clearfix')
        for sep_val in sepcs_values:
            spec = sep_val.css('dl.clearfix dt::text').get()
            value = ""
            value = sep_val.css('dl.clearfix dd::text').get()
            if(not value):
                # print("gpuname", gpuname ,"spec:",spec,"value:",value)
                value = sep_val.css('dl.clearfix a::text').get()
            if(not value):
                print("gpuname", gpuname ,"spec:",spec,"value:",value)
                value = ""
            self.my_dict[gpuname][spec] = value.replace("\n","").replace("\t","").replace("\r","")
            # for i in range(len(sepcs)):
                # self.my_dict[gpuname][sepcs[i]] = values[i]
        # values = response.css('dl.clearfix dd::text').getall()
        # for i in range(len(sepcs)):
            # self.my_dict[gpuname][sepcs[i]] = values[i]
            # break
        # print("my_dict:",self.my_dict)
        # json.dumps(self.my_dict)
        json.dump( self.my_dict, open( "AMD.json", 'w' ) )
    

# mytag::text
