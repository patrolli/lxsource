# Author: Li Xunsong
# Email: lixunsonghcl@126.com
# 创建一个 logger, 希望这个 logger 在项目所有文件中可用，能不能避免以参数传递的方式在所有文件中共享呢？在 logging 文件里面创建一个实例，在其他文件 import 之
# logging 的文件命名要有意义，同时避免冗余
import logging


def create_log(log_fpath=None):
    # get a logger
    # set two handler
    # registry the handler to the logger
    # set the record format
    # return the logger
    pass

