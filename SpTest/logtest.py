#coding=utf-8

import logging
import time
import os


def my_log(name):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关
    # logger.setLevel(logging.DEBUG)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/Log/'#输出日志的路径，需要提前添加log文件夹   os.path.dirname(os.getcwd())输出上一级路径
    log_name =  log_path + name + rq + '.log'#输出日志的文件名称
    # logfile = log_name
    fh = logging.FileHandler(log_name, mode='a+')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)


    print( os.getcwd()) #输出当前路径

import logging
import os
import time

class Log(object):
 def __init__(self, name=__name__, path='mylog.log', level='DEBUG'):
      self.__name = name
      self.__path = path
      self.__level = level
      self.__logger = logging.getLogger(self.__name)
      self.__logger.setLevel(self.__level)


 def __ini_handler(self):
      """初始化handler"""
      stream_handler = logging.StreamHandler()
      file_handler = logging.FileHandler(self.__path, encoding='utf-8')
      return stream_handler, file_handler


 def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
      """设置handler级别并添加到logger收集器"""
      stream_handler.setLevel(level)
      file_handler.setLevel(level)
      self.__logger.addHandler(stream_handler)
      self.__logger.addHandler(file_handler)


 def __set_formatter(self, stream_handler, file_handler):
      """设置日志输出格式"""
      formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
              '-%(levelname)s-[日志信息]: %(message)s',
              datefmt='%a, %d %b %Y %H:%M:%S')
      stream_handler.setFormatter(formatter)
      file_handler.setFormatter(formatter)

 def __close_handler(self, stream_handler, file_handler):
      """关闭handler"""
      stream_handler.close()
      file_handler.close()

 @property
 def Logger(self):
      """构造收集器，返回looger"""
      stream_handler, file_handler = self.__ini_handler()
      self.__set_handler(stream_handler, file_handler)
      self.__set_formatter(stream_handler, file_handler)
      self.__close_handler(stream_handler, file_handler)
      return self.__logger


if __name__ == '__main__':

    log_path = os.path.dirname(os.getcwd()) + '/Log/'
    log = Log(log_path, log_path+"file.log")
    logger = log.Logger
    logger.debug('I am a debug message')