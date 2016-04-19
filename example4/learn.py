

import sys
sys.path.insert(0, "../")
import codecs
import shelve

from aiml.LangSupport import mergeChineseSpace


db = shelve.open("simple_rules.db", "c", writeback=True)

template = """<?xml version="1.0" encoding="UTF-8"?>
<aiml version="1.0">

<meta name="author" content="autogen"/>
<meta name="language" content="zh"/>
{rules}
</aiml>
"""

category_template = """
<category>
<pattern>{pattern}</pattern>
<template>
{answer}
</template>
</category>
"""

#print sys.argv
if len(sys.argv) == 3:
    _, rule, temp = sys.argv
    # rule = mergeChineseSpace(str(rule, 'utf8'))
    # temp = mergeChineseSpace(str(temp, 'utf8'))
    db[rule] = temp
    db.sync()
    rules = []
    for r in db:
        rules.append(category_template.format(pattern=r,
                                              answer=db[r]))
    content = template.format(rules = '\n'.join(rules))
    with open("auto-gen.aiml", 'w', encoding='utf-8') as fp:
        fp.write(content)
