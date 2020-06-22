#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/4/24 10:36
import pymysql

class MysqlDB():

    def connection_db(self):
        """连接数据库"""
        db = pymysql.connect(host="192.168.30.36",
                             port=3306,
                             # db='pythonDB',
                             user="prodba",
                             password="12wsxCDE#",
                             charset="utf8")
        return db

    def connection(self):
        '''获取游标'''
        cursor = self.connection_db().cursor()
        return cursor

    def Create_library(self,name):
        '''创建库名'''
        cursor = self.connection()
        cursor.execute("CREATE DATABASE IF NOT EXISTS '%s' DEFAULT CHARSET utf8 "
                       "COLLATE utf8_general_ci;"%name)
        return

    def Create_table(self,name):
        '''创建表'''
        cursor = self.connection()
        db = self.connection_db()
        cursor.execute("drop table if exists '%s' " % name)
        sql = """CREATE TABLE IF NOT EXISTS '%s'  % name (
              'id' int(11) NOT NULL AUTO_INCREMENT,
              'orderName' varchar(255) NOT NULL,
              'orderid' int(11) NOT NULL,
               PRIMARY KEY ('id')
            ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
        '''提交'''
        db.commit(sql)
        '''关闭游标'''
        cursor.close()
        '''关闭数据库'''
        db.close()
        return

    def Query(self,sqls):
        '''查询数据'''
        db = self.connection_db()
        cursor = self.connection()
        # sql = (""" select * from the_order
        # where dy_mch_no = "%s" ;"""%dy_mch_no)
        sql = (sqls)
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                id = row[0]
                orderid = row[1]
                orderName = row[2]
                time = row[4]
                return id ,orderid,orderName,time
        except:
            print('数据不存在：%s'%sqls)
        cursor.close()
        db.close()

    def insert_db(self,orderid,orderName,time):
        '''新增数据'''
        con = self.connection()
        cur = con.cursor()
        try:
            sql = ("INSERT INTO user(orderid,orderName,time) VALUES('%d','%s','%s')"
                   %(orderid,orderName,time))
            cur.execute(sql)
            con.commit()
            return True
        except:
            con.rollback()
            raise
        finally:
            cur.close()
            con.close()

    def update_db(self,id,orderid):
        con = self.con_db()
        cur = con.cursor()
        try:
            str = ("UPDATE user SET id = %d WHERE username = '%s'"%(id,orderid))
            cur.execute(str)
            con.commit()
            return True
        except:
            con.rollback()
            raise Exception
        finally:
            cur.close()
            con.close()

    def delete_db(self,name):
        '''删除数据'''
        con = self.connection_db()
        cur = con.cursor()
        try:
            str = ("DELETE FROM user WHERE username = '%s'" % (name))
            cur.execute(str)
            con.commit()
            return True
        except:
            con.rollback()
            raise Exception
        finally:
            cur.close()
            con.close()

if __name__ == '__main__':

     mysql = MysqlDB()
     quer = mysql.Query("""select * from shdy_agent_foreign.t_trans_log_info where trade_code='P00' and trans_status =2 and trans_date>20200501
""")
     print(quer)
     # insert = mysql.insert_db(1321432,'ceshi',20201920)
     # print(" 新增成功 " )






