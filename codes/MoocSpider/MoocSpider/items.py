# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoocspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 课程名称
    name = scrapy.Field()
    # 课程主讲
    author = scrapy.Field()
    # 报名人数
    num = scrapy.Field()
    # 标签（如国家精品）
    label = scrapy.Field()
    # 学校
    university = scrapy.Field()
    # 学习进度
    process = scrapy.Field()
    pass
