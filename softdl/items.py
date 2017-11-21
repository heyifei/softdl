# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoftdlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    swname = scrapy.Field()
    swsize = scrapy.Field()
    swlanguge = scrapy.Field()
    swupdate = scrapy.Field()
    swauth = scrapy.Field()
    #wsplatform = scrapy.Field()
    swscore = scrapy.Field()
    swdevelop = scrapy.Field()
    swdetail = scrapy.Field()
    swdowntimes = scrapy.Field()
