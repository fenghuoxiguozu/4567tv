# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TvPipeline(object):
    def process_item(self, item, spider):
        return item


class RedisPipeline(object):
    def process_item(self, item, spider):
        dict={
            'title':item['title'],
            'url':item['url'],
            'introduce':item['introduce']
        }

        con = spider.con
        con.lpush('movie_data',dict)
        return item