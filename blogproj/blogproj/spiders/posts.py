# -*- coding: utf-8 -*-
import scrapy

from ..items import BlogprojItem
class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ["quotes.toscrape.com/"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class = "quote"]')
        item = BlogprojItem()
        for quote in quotes:
            item['Text'] = quote.xpath('.//*[@class="text"]/text()').extract_first()
            item['Author'] = quote.xpath('.//*[@class="author"]/text()').extract_first()
            item['Tag'] = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
            yield item


        # 	yield{'Text':text,
        # 		  'Author':author,
        # 		  'Tag':tag}

        	next_page_url=response.xpath('//*[class="next"]/a/@href').extract_first()
        	absolute_url=response.urljoin(next_page_url)
        yield scrapy.Request(absolute_url)

        # h1_tag = response.xpath('//h1/a/text()').extract()

        # tag = response.xpath('//*[@class="tag-item"]/a/text()').extract() 

        # yield {"H1_tag": h1_tag, 'Tag': tag }