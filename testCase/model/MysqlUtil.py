# -- coding: utf-8 --
#从数据库中获取测试数据
import pymysql


class MyMySQL():
    @classmethod
    def __init__(cls, host, port, dbName, username, password, charset):
        #进行数据库初始化
        cls.conn = pymysql.connect(
            host = host,
            port = port,
            db = dbName,
            user = username,
            passwd = password,
            charset = charset
        )
        # 获取数据库游标
        cls.cur = cls.conn.cursor()

    #获取执行sql后返回的查询结果
    @classmethod
    def getDataFromDataBases(cls,tarSql):
        #从testdata表中获取需要的测试数据
        #bookname作为搜索关键词，author作为预期关键词
        cls.cur.execute(tarSql)#执行指定的sql
        #从查询区域取回所有的查询结果
        datasTuple = cls.cur.fetchall()
        return datasTuple

    @classmethod
    def closeDatabase(cls):
        #数据库后期清理工作
        cls.cur.close()
        # self.conn.commit()
        cls.conn.close()

if __name__ == '__main__':
