# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from movie.items import MovieItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    #获取详情页链接
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        #print(movies)
        
        for movie in movies[0:10]:
            item = MovieItem()
            title = movie.xpath('./a/text()').extract_first()
            link = 'https://maoyan.com' + movie.xpath('./a/@href').extract_first()
            #print(title)
            #print(link)
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
    
    def parse2(self,response):
        item = response.meta['item']
        info = Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul')
        genres = info.xpath('./li[1]/*/text()').extract()
        #print(genres)
        #item['genres'] = '/'.join(genres)
        date = info.xpath('./li[3]/text()').extract_first()

        #print(f'电影类型: {genres}')
        #print(f'上映日期: {date}')
        item['genres'] = genres
        item['date'] = date
        yield item