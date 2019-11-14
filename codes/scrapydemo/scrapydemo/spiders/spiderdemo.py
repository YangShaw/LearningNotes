# -*- coding: utf-8 -*-
import scrapy


class SpiderdemoSpider(scrapy.Spider):
    name = 'spiderdemo'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    # 对response内容进行解析
    def parse(self, response):
        filename = response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('saved file %s.' % filename)

