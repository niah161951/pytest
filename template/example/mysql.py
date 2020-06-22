# -*- coding: utf-8 -*-
# 作者   : Lenovo
# 时间   : 2020/4/22 15:02
import logging,pymysql

class MYSQL_DB:

    def __init__(self):
        self.cursor = None

    @staticmethod
    def connect():
        try:
            con = pymysql.connect(host="192.168.20.170",port=3306,db='pythonDB',user="root",
                       password="12wsxCDE#",charset="utf8")

        except Exception as e:
            logging.info(e)
            return False

        return con

    def _cursor(self):
        return self.connect.cursor()

    def execute(self, sql):
        self.cursor = self._cursor()
        self.cursor.execute(sql)

    @staticmethod
    def to_json(result):

        _list = []
        for l in result:
            _list.append(list(l))

        return _list

    def sql_fetch_json(self):

        keys = []
        for column in self.cursor.description:
            keys.append(column[0])
        key_number = len(keys)

        json_data = []
        for row in self.cursor.fetchall():
            item = dict()
            for q in range(key_number):
                item[keys[q]] = row[q]
            json_data.append(item)

        self.closed()
        return json_data

    def closed(self):
        self.cursor.close()


if __name__ == '__main__':
    db = MYSQL_DB()
    db.execute(
       '''select mal_sub,ntf_to,val_lst from 
       (select * from CGDGW.T_NTC_EVTREC  order BY TM_SMP DESC ) where rownum <= 6'''
    )
    res = db.sql_fetch_json()[0]
    print(res)