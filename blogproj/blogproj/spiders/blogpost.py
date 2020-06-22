import scrapy


class BlogPostSpider(scrapy.Spider):
    name = "post"
    allowed_domain = "www.craigslist.org"
    start_urls = ["https://newyork.craigslist.org/search/egr"]


def parse(self, response):
    titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
    print(titles)
