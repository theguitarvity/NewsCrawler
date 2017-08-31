import scrapy
class FacomSpider(scrapy.Spider):
    name = 'facom'
    
    start_urls =['http://facom.ufms.br/noticias'] 
    def parse(self, response):
        for quote in response.css('div.media-body'):
            yield{
                
                'text': quote.css('p::text').extract_first().encode('utf-8'),
                'title': quote.css('h4.media-heading a::text').extract_first().encode('utf-8'),
            }   