# Author:ZhaoKang
# 用户认证装饰器
import logging.config
from conf import settings


def outer(func):
    from core import src
    def inner(*args, **kwargs):
        # 装饰之前干的事情
        if src.user_state['name']:
            result = func(*args, **kwargs)
            # 装饰之干的事情
            return result
        else:
            src.login()  # 如果用户没有登陆则跳入登陆的接口

    return inner


# 获取日志功能实例
def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)  # 创建log实例
    return logger
