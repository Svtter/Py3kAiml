import jieba

test = jieba.dt

print ("/ ".join(test.cut("我来到北京清华大学", cut_all=True)))
