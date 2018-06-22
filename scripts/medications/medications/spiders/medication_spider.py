import scrapy

import scrapy


class MedicationSpider(scrapy.Spider):
    name = "medication"

    start_urls = [
        'https://www.rxlist.com/drugs/alpha_a.htm',
        ]

    def parse(self, response):
        
        next_pages = response.css('#Drugs_AZlist li a::attr("href")').extract()

        for next_page in next_pages:
            
            yield response.follow(next_page, self.parse2)
            
            
    def parse2(self, response):
        for medication in response.css('.contentstyle ul li'):
            yield {
                'name': medication.css('a::text').extract_first(),
                'source': medication.css('span::text').extract_first()[2:],
                }

        # for medication in response.css('.contentstyle ul li'):
        #     yield {
        #         'name': medication.css('a::text').extract_first(),
        #         'source': medication.css('span::text').extract_first()[2:],
        #     }

        #Probably leads to an infinite loop, too lazy to check, probably should fix instead of hardcode
        # next_pages = response.css('#Drugs_AZlist li a::attr("href")').extract()
        
        # for next_page in next_pages:
        #     if next_page is not None :
        #         yield response.follow(next_page, self.parse)