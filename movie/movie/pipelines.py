# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def __init__(self):
        self.sess = DBSession()

    def process_item(self, item, spider):
        try:
            # print (obj)
            title = item["title"]
            mainpeople = item["mainpeople"]
            url = item["url"]
            moviess = Movie(title=title, mainpeople=mainpeople, url=url)
            self.sess.add(moviess)
            self.sess.commit()
            print ("存入数据库成功")
            return item

        except Exception as e:
            print ("存入数据库失败！！！，e",e)

    def close_spider(self,spider):
        self.sess.close()
        print ("关闭爬虫")










from sqlalchemy import Column,String,Integer,create_engine,ForeignKey,DateTime
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:root@localhost:3306/movies?charset=utf8')
DBSession = sessionmaker(bind=engine)

# session = DBSession()

class Movie(Base):
    __tablename__ = 'movie_movie'

    id = Column(Integer(), primary_key=True)
    title = Column(String(100), default = '')
    mainpeople = Column(String(255),  default = '')
    url = Column(String(255),  default = '')
    add_time = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return self.title + '--' + str(self.add_time)





class MoviePipeline2(object):
    def process_item(self, item, spider):
        with open('movie.txt', 'a+') as fp:
            try:
                fp.write(item["title"] + '---------'+item["url"]+'\n')
                print ('存入成功')
            except Exception as e:
                print ("存入数据库失败！！！，e",e)

    def close_spider(self,spider):
        print ("关闭爬虫")
