# 开发者：Pabi
# 开发时间：2023/1/19 21:50

import logging
import os.path
import time
import colorlog

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径v
log_path = os.path.join(root_path, 'log')


class Logger:

    # 初始化方法
    def __init__(self):

        # 设置颜色
        log_colors_config = {
            'DEBUG': 'white',  # cyan white
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }

        # 定义日志位置和文件名
        self.logname = os.path.join(log_path, "{}.log".format(time.strftime("%Y-%m-%d")))
        # 定义一个日志容器
        self.logger = logging.getLogger("log")
        # 设置日志打印的级别
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.INFO)
        # self.logger.setLevel(logging.WARNING)
        # self.logger.setLevel(logging.ERROR)

        # 创建日志输入的格式，Formatter就是格式化，时间+py文件名+行数+日志级别+报错信息
        self.formater = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        self.console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=log_colors_config
        )
        # self.console_formatter = colorlog.ColoredFormatter('%(log_color)s[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s', log_colors=log_colors_config)

        # 创建日志处理器，用来存放日志文件
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()

        # 设置控制台打印日志界别
        self.console.setLevel(logging.DEBUG)
        # self.console.setLevel(logging.INFO)
        # self.console.setLevel(logging.WARNING)
        # self.console.setLevel(logging.ERROR)

        # 文件存放日志级别
        self.filelogger.setLevel(logging.DEBUG)
        # self.filelogger.setLevel(logging.INFO)
        # self.filelogger.setLevel(logging.WARNING)
        # self.filelogger.setLevel(logging.ERROR)

        # 文件存放日志格式
        self.filelogger.setFormatter(self.formater)

        # 控制台打印日志格式
        self.console.setFormatter(self.formater)
        self.console.setFormatter(self.console_formatter)

        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


# 实例化容器logger
logger = Logger().logger

# if __name__ == '__main__':
#     logger.info("---测试开始---")
#     logger.debug("---测试结束---")