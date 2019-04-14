# Author:ZhaoKang
from DB import dbhelp
from lib import common
logger = common.get_logger('bank')


# 提现接口
def withdraw_interface(name, money):
    select_user_dic = dbhelp.select(name)
    # 判断用户余额是否大于提现金额 * 1.05
    money2 = money * 1.05
    money3 = money * 0.05
    if select_user_dic['balance'] >= money2:

        select_user_dic['balance'] -= money2

        info = '用户: [%s] 提现[%s$]！手续费: [%s]' % (name, money, money3)
        logger.info(info)

        # 记录提现流水
        select_user_dic['flow'].append(info)  # []

        dbhelp.save(select_user_dic)

        return True, info

    else:
        return False, '尊敬的用户，您的余额不足，请充值!'


# 请输入转账接口
def transfer_interface(from_name, to_name, money):
    to_user_dic = dbhelp.select(to_name)
    if not to_user_dic:
        return False, '目标用户不存在!'

    # 2、查询转账用户余额是否足够
    # 3、开始转账
    from_user_dic = dbhelp.select(from_name)
    if from_user_dic['balance'] >= money:

        from_user_dic['balance'] -= money
        to_user_dic['balance'] += money

        # 更新用户信息
        dbhelp.save(from_user_dic)
        dbhelp.save(to_user_dic)
        logger.info('用户[%s] 转账给 用户[%s] %s $!' % (from_name, to_name, money))
        return True, '用户[%s] 转账给 用户[%s] %s $!' % (from_name, to_name, money)
    else:
        return False, '尊敬的穷逼，您的余额不足，请充值!'


# 还款接口
def repay_interface(name, money):
    select_user_dic = dbhelp.select(name)
    select_user_dic['balance'] += money
    dbhelp.save(select_user_dic)
    logger.info('还[%s]$款成功!' % money)
    return '还[%s]$款成功!' % money


# 查看流水接口
def check_flow_interface(name):
    select_user_dic = dbhelp.select(name)
    return select_user_dic['flow']


# 支付接口
def pay_interface(name,cost):
    user_dic = dbhelp.select(name)

    if user_dic['balance'] >= cost:

        user_dic['balance'] -= cost

        user_dic['shopping_cart'] = {}

        dbhelp.save(user_dic)
        logger.info('支付成功')
        return True, '支付成功!'

    else:
        return False, '消费失败!'
