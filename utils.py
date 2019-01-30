# encoding: utf-8
# using Python 3.7

"""
通用工具包模块
"""

import random
import distutils.util

import itchat

config_dict = {}

def get_config(key):
    global config_dict

    if len(config_dict) == 0:
        with open('config.txt', 'r', encoding='utf-8') as f:
            for config_item in f.readlines():
                config_item = config_item.split('=')
                _key = config_item[0].strip()
                _value = config_item[1].strip()
                config_dict[_key] = _value

    result = config_dict[key]
    if result in ('True', 'False', 'true', 'false'):
        result = str_to_bool(result)
    return result

def get_random_message():
    with open('messages.txt', 'r', encoding='utf-8') as f:
        msg_list = f.readlines()
    return msg_list[random.randint(0, len(msg_list)-1)]

def send(content, user=None, type=None):
    result = False

    if type == 'f':
        result = itchat.send_file(fileDir=content, toUserName=user)
    elif type == 'p':
        result = itchat.send_img(fileDir=content, toUserName=user)
    elif type == 'v':
        result = itchat.send_video(fileDir=content, toUserName=user)
    else:
        result = itchat.send_msg(msg=content, toUserName=user)

    return result

def str_to_bool(str):
    return bool(distutils.util.strtobool(str))
