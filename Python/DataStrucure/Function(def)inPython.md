## self in def
self指的是实例Instance本身，而非类。

### 在继承时，传入的是哪个实例，就是那个传入的实例，而不是指定义了self的类的实例。
```
class Parent:
    def pprt(self):
        print(self)

class Child(Parent):
    def cprt(self):
        print(self)
c = Child()
c.cprt()
c.pprt()
p = Parent()
p.pprt()


Result:
<__main__.Child object at 0x0000000002A47080>
<__main__.Child object at 0x0000000002A47080>
<__main__.Parent object at 0x0000000002A47240>
```

## __init__
构造函数

## __name__ 和 __main__
模块是对象，并且所有的模块都有一个内置属性 __name__。  
一个模块的 __name__ 的值取决于您如何应用模块。  
如果 import 一个模块，那么模块__name__ 的值通常为模块文件名，不带路径或者文件扩展名

#### 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。


