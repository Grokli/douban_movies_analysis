# -*- coding: utf-8 -*-
from scrapy import cmdline


cmdline.execute('scrapy crawl douban -o movies.csv -s FEED_EXPORT_ENCODING=gbk'.split())