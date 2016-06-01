# encoding: utf-8

import jieba

__author__ = 'svtter'


# 立即初始化jieba
class SplitWord:

    def __init__(self):
        jieba.initialize()
        self.dt = jieba.dt

    def splitChinese(self, sentence, cutAll=False):
        '''
        cutall为false为精确模式，即分词合并还是句子
        '''
        # TODO: 标点符号分字
        seg_list = jieba.lcut(sentence, cut_all=cutAll)
        seg_list = self.filterpuntl(seg_list)
        mid = ' '.join(seg_list)
        after = list()
        after.append(mid)
        # logging.debug("splitChinese: ", seg_list, mid, after)
        return after
        # return seg_list

    def mergeChineseSpace(self, sentence):
        return ''.join(list(filter(lambda x: x != ' ', sentence)))

    def filterpuntl(self, seg_list):
        def judgein(x):
            return x not in punct
        punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
        ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
        々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
        ︽︿﹁﹃﹙﹛﹝（｛“‘-—…''')
        return list(filter(judgein, seg_list))

split = SplitWord()
splitChinese = split.splitChinese
mergeChineseSpace = split.mergeChineseSpace
dt = split.dt


if __name__ == '__main__':
    text = input()
    print(splitChinese(text))
