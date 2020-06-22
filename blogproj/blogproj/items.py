# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogprojItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Text = scrapy.Field()
    Author  = scrapy.Field()
    Tag =scrapy.Field()
