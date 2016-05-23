#!/usr/bin/env python
# coding: utf-8

'''
1. 提取所有问题到idf-question
'''


# 提取所有Q开头
with open('idf-question', 'w') as output:
    with open('data-simple', 'r') as f:
        for line in f.readlines():
            if line.startswith("Q："):
                output.write(line)


'''
生成idf词典
'''

import jieba
import jieba.analyse


# 生成字典
with open('idf-dict', 'w') as output:

    with open('idf-question', 'r') as content:
        tags = jieba.analyse.extract_tags(content.read(), topK=10, withWeight=True)

    for tag in tags:
        output.write("%s\t\t %f\n" % (tag[0], tag[1]))
