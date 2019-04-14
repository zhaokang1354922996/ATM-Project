# Author:ZhaoKang

from DB import dbhelp
from conf import settings
from lib import common

logger = common.get_logger('user')


# 注册接口
def register_interface(name, pwd, balance=15000):
    select_user_dic = dbhelp.select(name)
    if select_user_dic:
        if select_user_dic['name'] == name:
            logger.info('用户: [%s] 已存在!' % name)
            return False, '用户已经存在，请去登陆界面完成登陆吧'
    else:
        user_dic = {
            'name': name, 'pwd': pwd, 'balance': balance, 'flow': [], 'shop_cat': {}
        }
        dbhelp.save(user_dic)
        return True, '注册成功'


# 登陆接口
def login_interface(name, pwd):
    select_user_dic = dbhelp.select(name)
    if not select_user_dic:
        return False, '用户不存在'
    if select_user_dic['pwd'] == pwd:
        logger.info('用户: [%s] 登陆成功!' % name)
        return True, '登陆成功'

    else:
        logger.info('用户: [%s] 密码错误!' % name)
        return False, '密码错误'


# 查看用户余额接口
def check_balance_interface(name):
    select_user_dic = dbhelp.select(name)
    if not select_user_dic['balance']:
        return True, '你的余额不足'
    return True, select_user_dic['balance']


# 注销接口
def logout_interface():
    from core import src
    src.user_state['name'] = None
    return '注销成功'
