import scrapy
import json
import time
import random


class BooksSpider(scrapy.Spider):
    name = 'books'
    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES' : {
    #        'bookscraper.middlewares.CustomProxyMiddleware': 350,
    #     },
    # }
    my_dict = {}
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]

    def start_requests(self):
        # url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
        # url = 'https://www.techpowerup.com/gpu-specs/?mfgr=AMD&mobile=No&igp=No&sort=name'
        url = 'https://www.techpowerup.com/gpu-specs/?mfgr=NVIDIA&mobile=No&workstation=No&igp=No&sort=name'
        yield scrapy.Request(url, callback=self.parse,headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]})

    def parse(self, response):
        # item = {}
        pres = "https://www.techpowerup.com"
        count = 0
        for url in response.css('td.vendor-NVIDIA a::attr(href)').getall():
            print(pres+url)
            count += 1
            yield scrapy.Request(pres+url,  callback=self.parse_products,dont_filter=True,headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]})
            # if count > 2:
                # break
            time.sleep(1)
        

    def parse_products(self, response):
        pres = "https://www.techpowerup.com"
        for url in response.css('div.board-table-title__inner a::attr(href)').getall():
            print("url",url)
            yield scrapy.Request(pres+url ,callback=self.pasre_Gpu,
                                 dont_filter=True,headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]})
            time.sleep(1)
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
        json.dump( self.my_dict, open( "NVIDIA.json", 'w' ) )
    

# mytag::text
