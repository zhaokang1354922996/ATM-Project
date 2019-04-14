# Author:ZhaoKang
from interface import user
from conf import settings
import os.path
import json


def save(user_dic):
    with open('%s\%s.json' % (settings.DB_PATH, user_dic['name']), 'w', encoding='utf-8')as f:
        json.dump(user_dic, f)
        f.flush()


def select(name):
    user_path = '%s\%s.json' % (settings.DB_PATH, name)
    if not os.path.exists(user_path):
        return
    with open(user_path, 'r', encoding='utf-8')as f:
        user_dic = json.loads(f.read())
        return user_dic
