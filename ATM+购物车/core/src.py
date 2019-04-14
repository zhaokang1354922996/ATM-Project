# Author:ZhaoKang
from interface import user, bank, shop
from lib import common


# 用户登录状态
user_state = {'name': None}


# 注册
def register():
    print('欢迎来到注册界面！')
    txt = '请'
    while True:
        name = input(txt + '输入用户名:').strip()
        pwd = input(txt + '输入密码:').strip()
        repwd = input(txt + '确认密码:').strip()
        if pwd == repwd:
            flag, msg = user.register_interface(name, pwd)
            if flag:
                print(msg)
                login()
                break
            else:
                print(msg)
        else:
            txt = '请重新'
            print('你输入的非法')
            continue


# 登录
def login():
    print('欢迎来到登录界面！')

    while True:
        name = input('请输入用户名:').strip()
        if user_state['name'] == name:
            print('你输入的账号存在')
            return
        pwd = input('请输入密码:').strip()
        flag, msg = user.login_interface(name, pwd)
        if flag:

            user_state['name'] = name
            print(msg)
            break
        else:
            print(msg)
            register()


@common.outer
# 查看余额
def check_balance():
    print('欢迎来到查看余额界面！')
    flag, msg = user.check_balance_interface(user_state['name'])
    if flag:
        print(msg)
        return
    else:
        print(msg)


@common.outer
# 提现
def withdraw():
    print('欢迎来到提现界面！')
    while True:
        money = input('请输入提现金额: ').strip()
        if money.isdigit():
            money = int(money)
            flag, msg = bank.withdraw_interface(user_state['name'], money)
            if flag:
                print(msg)
                break

            else:
                print(msg)
        else:
            print('请输入数字!')


@common.outer
# 转账
def transfer():
    print('欢迎来到转账界面！')
    transfer_user = input('请输入目标用户:').strip()
    transfer_money = input('请输入转账金额:').strip()
    if transfer_money.isdigit():
        transfer_money = int(transfer_money)
    flag, msg = bank.transfer_interface(user_state['name'], transfer_user, transfer_money)
    if flag:
        print(msg)
    else:
        print(msg)


@common.outer
# 还款
def repay():
    print('欢迎来到还款界面！')
    while True:
        repay_money = input('请输入还款金额:').strip()
        repay_money = int(repay_money)
        msg = bank.repay_interface(user_state['name'], repay_money)
        print(msg)
        break


@common.outer
# 查看流水
def check_flow():
    print('欢迎来到查看流水界面！')
    msg = bank.check_flow_interface(user_state['name'])
    for line in msg:
        print(line)


@common.outer
# 购物车
def shop_cat():
    print('欢迎来到购物车界面！')
    goods_list = [
        ['iPhone 6', 2500],
        ['iPhone 6 Puls', 2900],
        ['iPhone 6s', 3200],
        ['iPhone 6s Puls', 3500],
        ['iPhone 7', 3700],
        ['iPhone 7 Puls', 3900],
        ['iPhone 8', 4200],
        ['iPhone 8 Puls', 5100],
        ['iPhone X', 6300],
        ['iPhone XR', 6500],
        ['iPhone XS MAX', 8300],
    ]
    user_balance = user.check_balance_interface(user_state['name'])
    shopping_cart = {}

    cost = 0
    while True:
        for index, i in enumerate(goods_list):
            print(index, i)
        choice = input('请输入商品编号:').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(goods_list):
                shop_name, shop_pice = goods_list[choice]
                if user_balance >= shop_pice:
                    if shop_name in shopping_cart:
                        shopping_cart[shop_name] += 1
                    else:
                        shopping_cart[shop_name] = 1
                    cost += shop_pice
                    flag, msg = shop.add_shop_cat(user_state['name'], shopping_cart)
                    if flag:
                        print(msg)
                        print(shopping_cart)
                else:
                    print('你的余额不足')
        elif choice == 'q':
            if cost == 0:
                break
            cofirm = input('确认购买输入Y/ N 取消:').strip()
            if cofirm == 'y':
                flag, msg = bank.pay_interface(user_state['name'], cost)
                if flag:
                    print(msg)
                    break

                else:
                    print(msg)


            else:
                print('退出购买!')
                break
        else:
            print('输入有误!')


@common.outer
# 查看购物车
def check_shop_cat():
    print('欢迎来到查看购物车界面！')
    check = bank.check_shop_cat_interface(user_state['name'])
    if check:
        print(check)
    else:
        print('你的购物车无商品')


@common.outer
# 注销用户
def logout():
    print('欢迎来到注销用户界面！')
    msg = bank.logout_interface()
    print(msg)


func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': transfer,
    '6': repay,
    '7': check_flow,
    '8': shop_cat,
    '9': check_shop_cat,
    '0': logout

}


def run():
    while True:
        print('''
        1、注册
        2、登录
        3、查看余额
        4、提现
        5、转账
        6、还款
        7、查看流水
        8、购物车
        9、查看购物车
        0、注销用户
        q、退出
        ''')
        choice = input('请输入你的选择:').strip()
        l = ['q', 'Q']
        if choice in l:
            break
        if choice in func_dic:
            func_dic[choice]()
        else:
            print('你输入的非法，请重新输入！')
