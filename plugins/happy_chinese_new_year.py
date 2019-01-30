# encoding: utf-8
# using Python 3.7

"""
拜年模块
"""

import os
import _thread

import utils

itchat = object

# send message to all friends
def send_all():
    global itchat
    print(itchat)
    friend_list = itchat.get_friends(update=True)

    for friend in friend_list:
        msg = utils.get_random_message()
        if not g_simulate_mode:
            utils.send(msg % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
        else:
            print('func send_all:', msg % (friend['DisplayName'] or friend['NickName']), friend['UserName'])

def run(_itchat):
    global itchat
    itchat = _itchat
    
    try:
        send_all()
    except Exception:
        pass
