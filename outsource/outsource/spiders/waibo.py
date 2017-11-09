# -*- coding: utf-8 -*-
import sys


import scrapy
import json
from outsource.items import OutsourceItem 

class CodingMartSpider(scrapy.Spider):
    # 启动 spider 的名字
    name = "waibo"

    ## 启始页
    start_urls = [
        'http://waibao.io/projects',
    ]

    # pof-list-item
    # 解析规则
    def parse(self, response):
        # yield json.load(response.body)
        items = []
        for htmlItem in response.css('div.card'):
            item = OutsourceItem()
            item['title'] = htmlItem.css('.card-title::text').extract_first() #.encode('utf-8')
            # item['url'] = 'http://waibao.io' + htmlItem.css('a::attr("href")').extract_first()
            item['price'] = htmlItem.css('.card-meta span::text').extract_first()
            item['summary'] = htmlItem.css('.card-body::text').extract_first()
            items.append(item)
        return items
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield response.follow(a, callback=self.parse)