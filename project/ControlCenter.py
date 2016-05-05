#!/usr/bin/env python
# coding: utf-8

__author__ = 'svtter'

import sys
sys.path.insert(0, "../")
import aiml


class ControlCenter:
    def __init__(self):
        self.status = "undefined"

    def command(self, cmd):
        pass

    def help(self):
        return '''
        本聊天机器人提供以下功能：

        1. help 查看帮助列表
        2. teach 学习
        3. consult 学习方法咨询
        4. search 查询题目
        5. exit 退出当前模式
        '''

    def teach(self):
        pass

    def consult(self):
        pass

    def search(self):
        pass

    def exit(self):
        self.status = "undefined"
