# Reflection in Python Python中的反射/自省

Reflection refers to the ability for code to be able to examine attributes about objects that might be passed as parameters to a function.  
For example, if we write type(obj) then Python will return an object which represents the type of obj.  

Using reflection, we can write one recursive reverse function that will work for strings, lists, and any other sequence that supports slicing and concatenation.  
If an obj is a reference to a string, then Python will return the str type object. Further, if we write str() we get a string which is the empty string. In other words, writing str() is the same thing as writing “”. Likewise, writing list() is the same thing as writing [].

Example：
```
#coding: UTF-8
import sys #  模块，sys指向这个模块对象
import inspect
def foo(): pass # 函数，foo指向这个函数对象
 
class Cat(object): # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name
    def sayHi(self): #  实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print self.name, 'says Hi!' # 访问名为name的字段，使用实例.name访问
 
cat = Cat() # cat是Cat类的实例对象
 
print Cat.sayHi # 使用类名访问实例方法时，方法是未绑定的(unbound)
print cat.sayHi # 使用实例访问实例方法时，方法是绑定的(bound)
```
当我们需要实现一个通用的DBM框架时，可能需要对数据对象的字段赋值，但我们无法预知用到这个框架的数据对象都有些什么字段，换言之，我们在写框架的时候需要通过某种机制访问未知的属性。
#### 
访问属性


## More： first line in python
```
#!/usr/bin/env python    <--- 告诉Linux/OS X系统这是一个Python可执行程序，Windows系统会忽略
#-*- coding: utf-8 -*-   
或者
#coding=utf-8            <--- 告诉Python解释器，按照UTF-8编码读取源代码，否则，在源代码中写的中文输出可能会有乱码
```
由于python源码文件默认编码方式是ascii 如果脚本中有非ascii编码的字符，而没有在脚本第一行或者第二行添加对应的编码方式的话，脚本执行的时候便会报错（只能是第一行或者第二行，其他行无效）

第一行其他例子：
```
#!/bin/sh           shell脚本
#!/usr/bin/perl     perl脚本
#!/usr/bin/python   python脚本
#!/usr/bin/python3  python3脚本
#!/usr/bin/python2  python2脚本
```

Reference:
PEP-0263
http://www.python.org/dev/peps/pep-0263/
vim语法文件编写总结
http://www.cnblogs.com/kohpoll/archive/2012/08/04/2623483.html
