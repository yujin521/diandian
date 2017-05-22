from  .sql import  Sql
from  dingdian.items import DingdianItem
from  dingdian.items import DcontentItem
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DingdianPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item,DingdianItem):
            name_id=item['name_id']
            ret=Sql.selcet_name(name_id)
            if ret[0]==1:
                print('已经存在了')
                pass
            else:
                name_id = item['name_id']
                xs_name=item['name']
                xs_author=item['author']
                category=item['category']
                Sql.intsert_dd_name(xs_name,xs_author,category,name_id)
                print('开始存小说标题')
        if isinstance(item,DcontentItem):
            url=item['chapterurl']
            name_id=item['id_name']
            num_id=item['num']
            xs_chaptername=item['chaptername']
            xs_content=item['chaptercontent']
            Sql.instert_dd_chaptername(xs_chaptername,xs_content,name_id,num_id,url)
            print('小说储存完毕')
            # return  item


