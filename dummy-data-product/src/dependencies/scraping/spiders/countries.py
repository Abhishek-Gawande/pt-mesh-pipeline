import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.aishub.net/']
    start_urls = ['https://www.aishub.net/stations']

    def parse(self, response):
        for i in range(1,20):

            scrapy.Request(url='https://www.aishub.net/stations?page={}'.format(i))
            
            rows=response.xpath("//table//tbody//tr")
            for row in rows:
                yield{
                'ID':row.xpath('td[1]//text()').extract_first(),
                'Status':row.xpath('td[2]//text()').extract_first(),
                'Uptime':row.xpath('td[3]//text()').extract_first(),
                'Country':row.xpath('td[4]//text()').extract_first(),
                'Location':row.xpath('td[5]//text()').extract_first(),
                'Ships':row.xpath('td[6]//text()').extract_first(),
                'Distinct':row.xpath('td[7]//text()').extract_first(),
                'Contributor':row.xpath('td[8]//text()').extract_first()
                }
            
