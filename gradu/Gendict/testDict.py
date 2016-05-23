#!/usr/bin/env python

import jieba
import jieba.analyse

'''
不做处理直接对问题答案进行idf分析
'''

content = open('data-simple', 'rb').read()
tags = jieba.analyse.extract_tags(content, withWeight=True)

for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
