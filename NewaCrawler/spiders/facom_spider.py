import scrapy
class FacomSpider(scrapy.Spider):
    name = 'facom'
    endereco = raw_input('digite a url')
    start_urls =[endereco] 
    def parse(self, response):
        for quote in response.css('div.media-body'):
            yield{
                
                'text': quote.css('p::text').extract_first().encode('utf-8'),
                'title': quote.css('h4.media-heading a::text').extract_first().encode('utf-8'),
            }   