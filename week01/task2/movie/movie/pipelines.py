# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline:
    def process_item(self, item, spider):
        title = item['title']
        genres = item['genres']
        date = item['date']
        SaveToFile = f'{title},{genres},{date}\n'
        with open('./maoyan_top10.csv','a+',encoding='utf-8') as Append:
            Append.write(SaveToFile)
        return item
