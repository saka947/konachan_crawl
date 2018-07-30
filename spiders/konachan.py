# -*- coding: utf-8 -*-
import scrapy
from ..items import PicItem
from scrapy import Request
from scrapy.loader import ItemLoader

class KonachanSpider(scrapy.Spider):
    name = 'konachan'
    allowed_domains = ['konachan.com']
    start_urls = ['https://konachan.com/post']
    pagemax = 10 #下载页数

    def __init__(self):
        self.page = 1

    def parse(self, response):
        xpath = '//*[@id="post-list-posts"]/li/a/@href'
        loader = ItemLoader(item=PicItem(), response=response)
        loader.add_xpath('image_urls',xpath)
        yield loader.load_item()
        next_page = 'https://konachan.com/post?page='+str(self.page)
        if self.page <= self.pagemax:
            self.page = self.page+1
            yield Request(url=next_page) #翻页




