# -*- coding: utf-8 -*-
import scrapy


class VideoDownloaderSpider(scrapy.Spider):
    name = 'video_downloader'
    allowed_domains = ['coursehunters.net', 'vs2.coursehunters.net']
    start_urls = ['https://coursehunters.net/course/linux-bash-shell-scripting-polnoe-rukovodstvo-vklyuchaya-awk-i-sed']

    def parse(self, response):   
        course_title = response.css('.hero-description::text').get()
        lessons_list = response.css('#lessons-list')
        
        for lesson_item in lessons_list.css('li.lessons-item'):
            lesson_name = lesson_item.css('div.lessons-name::text').get()
            lesson_video_url = lesson_item.css('link[itemprop=contentUrl]::attr(href)').get()
            print(lesson_name, lesson_video_url)
            
