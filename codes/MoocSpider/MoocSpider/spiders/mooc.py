# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from MoocSpider.items import MoocspiderItem
# splash lua script
script = """
         function main(splash, args)
             splash.response_body_enabled = true
             splash.private_mode_enabled = false
             assert(splash:go(args.url))
             assert(splash:wait(args.wait))
             
             return splash:html()
         end
         """

class MoocSpider(scrapy.Spider):
    name = 'mooc'
    url = 'https://www.icourse163.org/channel/3002.htm'

    # start request
    def start_requests(self):
        yield SplashRequest(self.url, callback=self.parse, endpoint='execute',
                            args={'lua_source': script, 'wait': 5})

    # parse the html content
    def parse(self, response):
        item = MoocspiderItem()

        all_course_module = response.xpath("//div[@class='_1gBJC']/div")
        courses = all_course_module.css("._2mbYw")

        for course in courses:

            university = course.css("._2lZi3::text").extract()
            name = course.css("h3::attr(title)").extract()
            author = course.css("._1Zkj9 span::text").extract()
            num = course.css("._3DcLu::text").extract()
            process = course.css(".hxvPL::text").extract()
            label = course.css("._3flBx span::text").extract()

            item['university'] = university
            item['name'] = name
            item['author'] = author
            item['num'] = num
            item['process'] = process
            item['label'] = label



            yield item

