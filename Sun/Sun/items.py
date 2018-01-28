# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SunItem(scrapy.Item):
    # define the fields for your item here like:
    # 编号
    number = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # url
    url = scrapy.Field()
    # 投诉内容
    content = scrapy.Field()
    pass
