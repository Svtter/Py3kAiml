#!/usr/bin/env python
# coding: utf-8

import jieba
import jieba.analyse

# jieba字典
jieba.load_userdict('dict.txt')

while True:
    content = input("> ")
    tags = jieba.analyse.extract_tags(content, topK=4)
    print(tags)
