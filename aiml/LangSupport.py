# encoding: utf-8

import jieba


# 立即初始化jieba

jieba.initialize()
dt = jieba.dt

__author__ = 'svtter'


def splitChinese(sentence, cutAll=False):
    '''
    cutall为false为精确模式，即分词合并还是句子
    '''
    # TODO: 标点符号分字
    seg_list = jieba.lcut(sentence, cut_all=cutAll)
    punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
    ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
    々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
    ︽︿﹁﹃﹙﹛﹝（｛“‘-—…''')
    filterpuntl = lambda l: list(filter(lambda x: x not in punct, l))
    seg_list = filterpuntl(seg_list)
    mid = ' '.join(seg_list)
    after = list()
    after.append(mid)
    # logging.debug("splitChinese: ", seg_list, mid, after)
    return after
    # return seg_list


def mergeChineseSpace(sentence):
    return ''.join(list(filter(lambda x: x != ' ', sentence)))


if __name__ == '__main__':
    text = input()
    print(splitChinese(text))
