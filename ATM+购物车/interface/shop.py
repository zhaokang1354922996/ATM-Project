# Author:ZhaoKang
from DB import dbhelp
from lib import common
logger = common.get_logger('shop')

# 添加购物车
def add_shop_cat(name, shopping_cart):
    user_dic = dbhelp.select(name)

    user_dic['shopping_cart'] = shopping_cart

    dbhelp.save(user_dic)
    logger.info('添加商品成功!')
    return True, '添加商品成功!'


def check_shop_cat_interface(name):
    user_dic = dbhelp.select(name)

    return user_dic['shopping_cart']
