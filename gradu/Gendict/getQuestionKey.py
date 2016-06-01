#!/usr/bin/env python
# coding: utf-8

'''
用于找出问题的关键词，使用简单的词典
'''


import jieba
import jieba.analyse

# jieba字典

FILE = 'test3.aiml'
TOPK = 2

jieba.load_userdict('dict.txt')
jieba.analyse.set_idf_path('idf.txt.big')

output = open(FILE, 'w')


def gentags(ele, content):
    return ("<"+ele+">\n") + (content) + ("</"+ele+">\n")


def writetags(ele, content):
    output.write("<"+ele+">\n")
    output.write(content)
    output.write("</"+ele+">\n\n")


pattern, templete = "", ""

with open('data-simple', 'r') as f:
    for line in f.readlines():
        if line.startswith("Q:"):
            tags = jieba.analyse.extract_tags(line, topK=TOPK)
            content = ("".join(tags))
            topk = TOPK
            while topk < 4:
                content += '*'
                topk += 1
            content += '\n'
            pattern = gentags('pattern', content)

        elif line.startswith("A:"):
            content = line[2:]
            templete = gentags('template', content)
            content = pattern + templete
            writetags('category', content)
            pattern, templete = "", ""


output.close()
