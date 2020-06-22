# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# # 作者   : Lenovo
# # 时间   : 2020/5/19 17:02
import logging
import logging.handlers
import os
import time
# import logging,time,os
#
# log_path = r"E:\下载"
# class Log:
#     '''
#     文件命名
#     '''
#     def __init__(self):
#         self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y%m%d'))
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.DEBUG)
#         self.formatter = logging.Formatter\
#             ('[%(asctime)s]-%[(filename)s]-%(levelname)s:%(message)s)')
#
#     def __console(self,level,message):
#
#         fh = logging.FileHandler(self.logname,'a',encoding='utf-8')#追加模式
#         fh.setLevel(logging.DEBUG)
#         fh.setFormatter(self.formatter)
#         self.logger.addHandler(fh)
#         '''创建StreamHandler()输出到控制台'''
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         ch.setFormatter(self.formatter)
#         self.logger.addHandler(ch)
#
#         if level == 'info':
#             self.logger.info(message)
#
#         elif level == 'debug':
#             self.logger.debug(message)
#
#         elif level == 'warning':
#             self.logger.warning(message)
#
#         elif level == 'error':
#             self.logger.error(message)
#         '''避免日志重复输出问题'''
#         self.logger.removeHandler(ch)
#         self.logger.removeHandler(fh)
#
#         fh.close()
#
#     def debug(self,message):
#         self.__console('debug',message)
#
#     def info(self,message):
#         self.__console('info',message)
#
#     def warning(self,message):
#         self.__console('warning',message)
#
#     def error(self,message):
#         self.__console('error',message)
#
# if __name__=="__main__":
#     log = Log()
#     log.info('------------------')
#     # log.info('1111111111111111111')
#     # log.warning('++++++++++++++++++++++')

class logs:

    def __init__(self):
        self.logger = logging.getLogger("")
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        # 创建文件目录
        logs_dir = "logs"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = '%s.txt' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

# if __name__ == '__main__':
#     logger=logging.getLogger()
#     logger.info("------------------")
#     logger.debug("-------===================")
#     logger.error("+++++++++++++++++")
#     logger.warning("+++++++++++++1111111111")