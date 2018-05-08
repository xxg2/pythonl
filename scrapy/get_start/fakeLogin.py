# -*- coding=UTF-8 -*-
import getpass

class FakeLogin(object):
    def __init__(self):
        self.name = 'king'
        self.password = 'haha'
        self.banner = 'Hello'
        self.run()

    def run(self):
        '''仿Linux终端窗口'''
        while True:
            print 'Login:king'
            pw = getpass.getpass('Password:')
            if pw == '88888888':
                print 'exit'
                exit()
            else:
                if len(pw) > 12:
                    print '密码长度应小于12'
                    continue
                elif len(pw) < 6:
                    print '密码长度应大于6'
                    continue
                else:
                    print '可惜'
                    continue