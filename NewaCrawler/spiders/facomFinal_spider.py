from neo4j.v1 import GraphDatabase
import scrapy

class FacomFinalSpider(scrapy.Spider):
    name = 'testeFinal'
    start_url = ['http://facom.ufms.br/noticias']

    def add_noticia(self, title, text):
        self.run("create(aa:Noticia{title:$title, text:$text})", title = title, text = text)
        print "Adicionado"
    
    def parse(self, response):
        driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","tpTxf&25"))
        
        for quote in response.css('div.media-body'):
            
            yield{
                'text': quote.css('p::text').extract_first(),
                'title': quote.css('h4.media-heading a::text').extract_first(),
            }
            title = quote.css('h4.media-heading a::text').extract_first()
            text = quote.css('p::text').extract_first()
            title = str(title)
            text = str(text)
            with driver.session() as session:
                session.write_transaction(add_noticia, title, text)
