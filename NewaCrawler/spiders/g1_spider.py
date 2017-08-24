import scrapy
class G1Scrapy(scrapy.Spider):
    name = 'g1'
    start_urls = [
        'http://g1.globo.com',
    
    ]
    def parse(self, response):
        for news in response.css('div._t'):
            yield {
                'texto': news.css('p.feed-post-body-title gui-color-primary gui-color-hover::text').extract_first(),
            }
