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
```
cat = Cat('kitty')
 
print cat.name # 访问实例属性
cat.sayHi() # 调用实例方法
 
print dir(cat) # 获取实例的属性名，以列表形式返回
if hasattr(cat, 'name'): # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger') # same as: a.name = 'tiger'
print getattr(cat, 'name') # same as: print a.name
 
getattr(cat, 'sayHi')() # same as: cat.sayHi()
```
#### dir([obj]): 
调用这个方法将返回包含obj大多数属性名的列表（会有一些特殊的属性不包含在内）。obj的默认值是当前的模块对象。
#### hasattr(obj, attr): 
这个方法用于检查obj是否有一个名为attr的值的属性，返回一个布尔值。
#### getattr(obj, attr): 
调用这个方法将返回obj中名为attr值的属性的值，例如如果attr为'bar'，则返回obj.bar。
#### setattr(obj, attr, val): 
调用这个方法将给obj的名为attr的值的属性赋值为val。例如如果attr为'bar'，则相当于obj.bar = val。
#### 

#### 模块：
__doc__: 文档字符串。如果模块没有文档，这个值是None。  
*__name__: 始终是定义时的模块名；即使你使用import .. as 为它取了别名，或是赋值给了另一个变量名。  
*__dict__: 包含了模块里可用的属性名-属性的字典；也就是可以使用模块名.属性名访问的对象。  
__file__: 包含了该模块的文件路径。需要注意的是内建的模块没有这个属性，访问它会抛出异常！  

#### 类：
__doc__: 文档字符串。如果类没有文档，这个值是None。
*__name__: 始终是定义时的类名。
*__dict__: 包含了类里可用的属性名-属性的字典；也就是可以使用类名.属性名访问的对象。
__module__: 包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象。
*__bases__: 直接父类对象的元组；但不包含继承树更上层的其他类，比如父类的父类。
```
print Cat.__doc__           # None
print Cat.__name__          # Cat
print Cat.__module__        # __main__
print Cat.__bases__         # (<type>,)
print Cat.__dict__          # {'__module__': '__main__', ...}</type>
```


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
https://www.cnblogs.com/huxi/archive/2011/01/02/1924317.html
