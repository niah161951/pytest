# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/2/19 21:26
import pymysql
def get_conn(): pass


from SHDY.Public.conf import Config

mch_no = Config().get_param('mercid')

class Mysql_connect():
    """
    初始化
    """
    def __init__(self,host,user,password,database):
        """
        :param host:        IP
        :param user:        用户名
        :param password:    密码
        :param database:    库名
        :param port:        端口号
        :param charset:     编码
        :return:
        """
        self.db = pymysql.connect(host= host,user=user,password=password,
                                  database=database,prot =3306,charset= 'utf8')
        self.cursor = self.db.cursor()
    #   插入数据，以元组的形式
        def exec_data(self,sql,data = None):
            # 执行sql语句
            self.csursor.execute(sql,data)
            # 提交到数据库执行
            self.db.commit()
        def exec(self,sql):
            self.cursor.execute(sql)
            self.db.commit()

        def select(self,sql):
            self.cursor.execute(sql)
            sele= self.cursor.fetchall()
            for row in sele:
                print(row)
        def cose(self):
            #关闭
            self.cursor.close()
            self.db.close()
if __name__ == '__main__':
    mysql = Mysql_connect('192.168.30.36','prodba','12wsxCDE#','shdy_agent_foreign')






