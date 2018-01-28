# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  Sun.items import SunItem


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    # 编辑允许的域名
    allowed_domains = ['sun0769.com']
    # 编辑起始的url
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    rules = (
        # 提取列表页面url的规则,需要在响应中继续应用链接提取器的时候需要将follow设置为True
        # 'index.php/question/questionType\?type=4&page=\d+'
        Rule(LinkExtractor(allow=r'questionType'), follow=True),
        # 'html/question/201801/359662.shtml'
        # 提取详情页面url的规则，需要从响应中解析数据的时候，添加callback，不需要解析数据就不用callback
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item'),

    )

    def parse_item(self, response):
        # print('----',response.url)
        # 创建存储数据的item实例
        item = SunItem()

        # 抽取数据
        item['url'] = response.url
        item['title'] = response.xpath('/html/head/title/text()').extract_first().split('_')[0]
        item['number'] = response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract_first().split(':')[-1].strip()
        item['content'] = response.xpath('/html/head/meta[@name="description"]/@content').extract_first()
        # print(item)

        # 返回数据
        yield item


