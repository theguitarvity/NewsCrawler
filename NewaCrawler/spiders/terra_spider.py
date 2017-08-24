import scrapy
class TerraSpider(scrapy.Spider):
    name = 'terra'
    start_urls = [
        'http://terra.com.br/',
    ]
    def parse(self, response):
        for news in response.css('div.cards'):
            yield {
                'text':news.css('div.title::text').extract_first()
            }