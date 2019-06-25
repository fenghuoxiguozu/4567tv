# -*- coding: utf-8 -*-
import scrapy
import hashlib
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tv.items import TvItem
from redis import Redis

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['4567tv.tv']
    start_urls = ['https://www.4567tv.tv/frim/index1.html']

    con=Redis(host='127.0.0.1',port=6379)

    rules = (
        Rule(LinkExtractor(allow=r'4567tv.tv/frim/index\d+.html'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'4567tv.tv/movie/index\d+.html'), callback='parse_detail', follow=False),
    )

    def parse_item(self, response):
        head_url='https://www.4567tv.tv'
        contents=response.xpath('//ul[@class="stui-vodlist clearfix"]/li')
        for c in contents:
            url =head_url+c.xpath('.//h4[@class="title text-overflow"]/a/@href').extract_first()

            # url=hashlib.sha256(url.encode()).hexdigest() 如果爬取大文本可保存hash
            ex=self.con.sadd('url',url)
            if ex==1:
                print('暂未爬取，开始爬取。。。。。')
                yield scrapy.Request(url=url,callback=self.parsr_detail)
            else:
                print('已爬取过')


    def parsr_detail(self,response):
        item = TvItem()
        item['title'] = response.xpath('//div[@class="stui-content__detail"]/h1[@class="title"]/text()').extract_first()
        item['introduce']=response.xpath('//p[@class="desc detail hidden-xs"]/span[@class="detail-sketch"]/text()').extract_first()
        item['url'] = response.url
        yield item