# encoding: utf-8
# using Python 3.7

import os
import _thread

import itchat

import utils
from plugins import auto_reply, happy_chinese_new_year, check_friendship

def show_config():
    print('---------config---------')
    print('unit_test:', utils.get_config('unit_test'))
    print('simulate_mode:', utils.get_config('simulate_mode'))
    print('------------------------')

def test():
    print()
    print('---------run test---------')
    print('func get_random_message:', utils.get_random_message())
    print('---------end test---------')
    print()

def run_plugin(plugin):
    print('load plugin:', str(plugin).split('\'')[1])
    _thread.start_new_thread(plugin.run, (itchat,))

def clean():
    os.system('cls')

def init():
    clean()
    itchat.auto_login(hotReload=True, enableCmdQR=2)

def script():
    clean()
    show_config()
    if utils.get_config('unit_test'):
        test()
    try:
        send_all()
    except Exception:
        pass
    run_plugin(auto_reply)
    run_plugin(happy_chinese_new_year)
    run_plugin(check_friendship)

def listen():
    itchat.run()

def main():
    init()
    script()
    # listen()

if __name__ == '__main__':
    main()
