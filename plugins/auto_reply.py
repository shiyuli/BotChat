# encoding: utf-8
# using Python 3.7

"""
简单回复模块
"""

import itchat as itchat_package
from itchat.content import TEXT

itchat = object

@itchat_package.msg_register(TEXT, isFriendChat=True)
def simple_reply(msg):
    return 'This is a simple reply from server.'

def run(_itchat):
    global itchat
    itchat = _itchat

    try:
        itchat.run()
    except Exception:
        pass
