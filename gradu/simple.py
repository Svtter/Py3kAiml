#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.insert(0, "../")

import aiml
import jieba.analyse


class AnswerBot:

    def __init__(self):

        self.kern = aiml.Kernel()
        self.dt = aiml.dt
        self.dt.load_userdict('Gendict/dict.txt')
        self.kern.bootstrap(learnFiles="cn-startup.xml",
                            commands="load aiml cn")

    def textin(self, text):
        if text.startswith('反馈'):
            self.writein(text[2:])
            return "您的问题已经反馈给管理员，将在后续陆续添加。"
        tags = jieba.analyse.extract_tags(text, topK=4)
        print(''.join(tags))
        return self.kern.respond(text)

    # TODO: 并发问题
    def writein(self, text):
        with open('feedback', 'w') as f:
            f.write(text+'\n')
