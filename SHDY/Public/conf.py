# _*_ coding: utf-8 _*_
# 作者    : 一蓑烟雨任平生 
# 创建时间 : 2019/12/30 15:28
import configparser

def get_str(s,f,b):
    '''
    获取特定字符串
    '''
    par = s.partition(f)
    return (par[2].partition(b))[0][:]

class Config:
    '''
    存贮数据  保存路径
    '''
    def __init__(self, file=r"D:/PycharmProject/untitled/SHDY/Public/orderId.txt"):
        self.file = file
        self.conf = configparser.ConfigParser()
        self.conf.read(file, encoding='gbk')

    def get_param(self,name):
        value=self.conf.get("订单号",name)
        return value

    def set_param(self,name,value):
        try:
            self.conf.add_section("订单号")
            self.conf.set("订单号",name,value)
            with open(self.file,'w') as f:
                self.conf.write(f)
                
        except configparser.DuplicateSectionError:
            self.conf.set("订单号", name, value)
            with open(self.file, 'w') as f:
                self.conf.write(f)


