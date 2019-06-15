##  Time 测试
```
import time
start_time = time.time()

def a():
    '''
    ....
    :return:
    '''
end_time = time.time()
print("test time:", end_time - start_time)
```

## Timeit 测试代码运行速度
```
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l.append(i)


def test2():
    l = [i for i in range(1000)]


def test3():
    l = []
    for i in range(1000):
        l.insert(len(l) - 1, i)
 
 
 def test4():
    l = []
    for i in range(1000):
        l += [i]


# timeit.Timer(statement, setup, timer)
# stmt参数是要测试的代码语句（statment）；
# setup参数是运行代码时需要的设置；
# timer参数是一个定时器函数，与平台有关。


t1 = Timer("test1()", "from __main__ import test1")  # 字符串内空格不能少
print("append: ", t1.timeit(number=10000), "seconds")
# append:  0.7832471559999999 seconds
t2 = Timer("test2()", "from __main__ import test2")
print("list comprehension: ", t2.timeit(number=10000), "seconds")
# list comprehension:  0.33927234100000003 seconds
t3 = Timer("test3()", "from __main__ import test3")
print("insert: ", t3.timeit(number=10000), "seconds")
# insert:  2.294977324 seconds
t4 = Timer("test4()", "from __main__ import test4")
print("+: ", t4.timeit(number=10000), "seconds")
# +:  1.3513635829999995 seconds
```
