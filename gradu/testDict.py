#!/usr/bin/env python

import jieba
import jieba.analyse

content = open('data', 'rb').read()
tags = jieba.analyse.extract_tags(content, withWeight=True)

for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
