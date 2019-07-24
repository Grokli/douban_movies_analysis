# -*- coding: utf-8 -*-
import scrapy
import json
from movies.items import MoviesItem
from copy import deepcopy

index = 1
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&year_range=2019,2019']

    def parse(self, response):
        global index
        data = json.loads(response.body.decode())
        data = data['data']
        if len(data)>0:
            for i in data:
                item = MoviesItem()
                item['title'] = i['title']
                item['rate'] = i['rate']
                item['star'] = i['star']
                url = i['url']
                yield scrapy.Request(url, callback=self.parse_detail, meta={'item':deepcopy(item)})
            next_url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}&year_range=2019,2019'.format(index*20)
            index += 1
            yield scrapy.Request(next_url, callback=self.parse)


    def parse_detail(self, response):
        item = response.meta['item']
        item['location'] = response.xpath('//div[@id="info"]/span[contains(text(),"制片")]/following-sibling::text()[1]').extract_first()
        item['location'] = item['location'].split('/') if item['location'] else ''
        item['language'] = response.xpath('//div[@id="info"]/span[contains(text(),"语言")]/following-sibling::text()[1]').extract_first()
        item['language'] = item['language'].split('/') if item['language'] else ''
        item['during_time'] = response.xpath('//div[@id="info"]/span[@property="v:runtime"]/@content').extract_first()
        item['types'] = response.xpath('//div[@id="info"]/span[@property="v:genre"]/text()').extract()
        short_comments = response.xpath('//div[@id="comments-section"]//span[@class="pl"]/a/text()').extract_first()
        short_comments = short_comments[2:-1] if short_comments  else 0 
        long_comments = response.xpath('//section[@class="reviews mod movie-content"]//span[@class="pl"]/a/text()').extract_first()
        long_comments = long_comments[2:-1] if long_comments  else 0
        item['comments'] = int(short_comments) + int(long_comments)
        yield item