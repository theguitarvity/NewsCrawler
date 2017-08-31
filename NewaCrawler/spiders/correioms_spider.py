import scrapy

class CorreioMSSpider(scrapy.Spider):
    name = 'correioms'
    start_urls = ['http://www.correiodoestado.com.br/cidades/campo-grande/']

    def parse(self, response):
        for quote in response.css('div.noticiaLink'):
            yield{
               'hora':quote.css('a.horaNoticia::text').extract_first(),
               'titulo': quote.css('a small::text').extract_first(),
               'previa': quote.css('a h3.tituloNoticiaLink::text').extract_first(),
            }