import scrapy
import json
class CodingMartSpider(scrapy.Spider):
    # 启动 spider 的名字
    name = "codingmart"

    ## 启始页
    start_urls = [
        'https://mart.coding.net/api/reward/list?page=1',
    ]
    # 解析规则
    def parse(self, response):
        # yield json.load(response.body)
        yield {
            'res': response.body
        }
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield response.follow(a, callback=self.parse)