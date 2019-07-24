# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rate = scrapy.Field()
    types = scrapy.Field()
    location = scrapy.Field()
    during_time = scrapy.Field()
    comments = scrapy.Field()
    star = scrapy.Field()
    language = scrapy.Field()
