# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutopjtPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self, item, spider):

        for j in range(0, len(item["name"])):
            # 将当前页的第 j 个商品的名称赋值给变量 name
            name = item["name"][j]
            price = item["price"][j]
            comnum = item["comnum"][j]
            link = item["link"][j]
            # 将当前页下第j个商品的 name、price、comnum、link 等信息处理一下
            # 重新组合成一个字典
            goods = {"name": name, "price": price, "comnum": comnum, "link": link}
            data = dict(goods)
            self.post.insert(data)
        return item