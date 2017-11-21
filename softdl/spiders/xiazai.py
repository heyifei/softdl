# -*- coding: utf-8 -*-
import scrapy
from softdl.items import SoftdlItem
from scrapy.http import Request


class XiazaiSpider(scrapy.Spider):
    name = 'xiazai'
    allowed_domains = ['www.xiazaiba.com']
    start_urls = ['http://www.xiazaiba.com/downlist/187_2.html']
    url_str = 'http://www.xiazaiba.com/downlist/187_'
    url_end = '.html'
    kv = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

    def start_requests(self):
        for i in range(2, 2100):
            url = self.url_str + str(i) + self.url_end
            yield Request(url, self.parse, headers=self.kv)

    def parse(self, response):
        r = response.xpath("//ul[@class='cur-cat-list']//li/a[1]/@href").extract()
        for rn in r:
            yield Request(rn, self.get_sw_detail, headers=self.kv)

    def get_sw_detail(self, response):
        item = SoftdlItem()
        item['swname'] = response.xpath("//div[@class='soft-title']/h1/text()").extract()
        #print(item['swname'])
        item['swsize'] = response.xpath("//ul[@class='clearfix']/li[1]/span/text()").extract()
        item['swlanguge'] = response.xpath("//ul[@class='clearfix']/li[2]/text()").extract()
        item['swupdate'] = response.xpath("//ul[@class='clearfix']/li[3]/text()").extract()
        item['swauth'] = response.xpath("//ul[@class='clearfix']/li[4]/text()").extract()
        #item['wsplatform'] = respon.xpath("//ul[@class='clearfix']/li[4]/text()")
        item['swscore'] = response.xpath("//ul[@class='clearfix']/li[6]/span[3]/i/text()").extract()
        item['swdevelop'] = response.xpath("//ul[@class='clearfix']/li[7]/a/text()").extract()
        item['swdetail'] = response.xpath("//td[@class='soft-content']/p/text()").extract()
        item['swdowntimes'] = response.xpath("//a[@id='base_download']/span/text()").extract()
        yield item

