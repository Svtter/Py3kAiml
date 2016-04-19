Py3kaiml
===

一个pyaiml的python3版本，支持中文。

借鉴了[andelf的工作](https://github.com/andelf/PyAIML)


feature
---

- 使用jieba分词，但是目前分词似乎没什么用处


Todo
---

- 与官方的todo暂时没有什么区别，具体可以查看[todo](todo.txt)
- 一些`andelf`修正的bug暂时没有去看，不知道在`py3kaiml`中是否存在

Example
---

例子完全是使用的`andelf`所使用的例子，支持情况尚可。


结语
---

这是我的毕业设计，今后（2016年4月19日）还会再更新，希望添加新的特性，作为一个强大的聊天机器人。


---

old readme
===

Updating the code for Python 3.2

Jason Ayres


PyAIML -- The Python AIML Interpreter
author: Cort Stratton (cort@users.sourceforge.net)
web: http://pyaiml.sourceforge.net/

PyAIML is an interpreter for AIML (the Artificial Intelligence Markup
Language), implemented entirely in standard Python.  It strives for
simple, austere, 100% compliance with the AIML 1.0.1 standard, no less
and no more.

This is currently pre-alpha software.  Use at your
own risk!

For information on what's new in this version, see the
CHANGES.txt file.

For information on the state of development, including 
the current level of AIML 1.0.1 compliance, see the
SUPPORTED_TAGS.txt file.

Quick & dirty example (assuming you've downloaded the
"standard" AIML set):

	import aiml

	# The Kernel object is the public interface to
	# the AIML interpreter.
	k = aiml.Kernel()

	# Use the 'learn' method to load the contents
	# of an AIML file into the Kernel.
	k.learn("std-startup.xml")

	# Use the 'respond' method to compute the response
	# to a user's input string.  respond() returns
	# the interpreter's response, which in this case
	# we ignore.
	k.respond("load aiml b")

	# Loop forever, reading user input from the command
	# line and printing responses.
	while True: print k.respond(str(input("> ")))
