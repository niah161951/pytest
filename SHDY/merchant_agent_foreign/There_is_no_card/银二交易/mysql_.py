# -*- coding: utf-8 -*-
# @The_author: Lenovo
# @Time    : 2020/2/14 10:33
import pymysql
from SHDY.Public.conf import Config

mch_no = Config().get_param('mercid')
#print(mch_no)

def get_conn():

    db = pymysql.connect(host = '192.168.30.36',user= 'prodba' ,port = 3306,
                           password= '12wsxCDE#',database='shdy_agent_foreign',charset = 'utf8')
    return db
def  quer_db():
    db = get_conn()
    #建立游标
    curdor = db.cursor()
    #执行sql
    sql = """
    select token from t_card_sign
    where mch_no = '%s',mch_no
    """
    # sql1 = """
    # SELECT trans_date,trans_time FROM t_trans_log_info
    # WHERE mer_order_no= '1234819213209600'
    # """
    curdor.execute(sql)
    # curdor.execute(sql1)
    #获取数据
    data = curdor.fetchall()
    print(data)
    #return  data
    curdor.close()
    db.close()
if __name__ == '__main__':
    quer_db()


