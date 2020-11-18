import scrapy

class QuotesSpider(scrapy.Spider):
    name="quotes"
    # name="jobs"
    def start_requests(self):
        urls=[
            'https://quotes.toscrapse.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
            # 'https://www.indeed.com/jobs',

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        page=response.url.split("/")[-2] #indicates the last but one character
        filename=f'quotes-{page}.html'
        #filename=f'jobs-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


