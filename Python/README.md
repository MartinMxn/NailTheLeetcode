# Skilllllllll in python

## For loop
```
list = [1,2,3]
1. for i in range(len(list)):
  ...
S = "some string"
2. for c in S:
  ...
3. for i, c in enumerate(dict/list/tuple)
enumerate() in python:
  like entry in Java
enumerate(sequence, [start=0])
4. book = {c : i for i, c in enumerate(order)}
list/dict/tuple comprehision
create a dict and with compression in one line
```

## List
```
.append() # at last
.pop() # pop last and get
```

## Set
返回一个新的 set 或 frozenset 对象，其元素来自于 iterable。 集合的元素必须为 **hashable。** ?  
无序，不重复序列
```
Creation: 
1.set1 = {"1", "2"}
2.convert from list 
  list1 = ["1", "2", "2", "1"]
  set2 = set(list1)
3.s = set()

String in set
>>> a = set("boy")
>>> a
{'y', 'o', 'b'}

len(s)
x in s / x not in s
add() 
remove() if not in, return key error
discard() if in, remove it
pop() random pop a element
clear()
isdisjoint(other s)
issubset(other s ) : s < other / s <= other
issuperset : s > other / s >= other
copy() 浅拷贝

```

## Sort
```
word = ["bca","a","b","ba",,"bda","bdca"]
word.sort(key = len)

for i in sorted(word, key = len):
  ...
```

## Built-in Functions
any(iterable) 
```
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```
all(iterable) # empty also true
```
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```
### getattr(object, name, [default])
```
Return the value of the named attribute of object. name must be a string. 
If the named attribute does not exist, default is returned if provided
otherwise **AttributeError** is raised.
```
setattr(object, name, value)
```
The arguments are an object, a string and an arbitrary value.
```
delattr(object, name)
```
The arguments are an object and a string.
# delattr(x, 'foobar') is equivalent to del x.foobar.
```
### next()/n() ??
```
Continue execution until the next line in the current function is reached or it returns.
```

### zip()
```
将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
```

### index()
```
Return the smallest index / the first occurrence of x in the array.
Otherwise, return a ValueError.
```

## yield 表达式 ??
把一个函数变成一个生成器generator
用来延迟，在需要时候再产生结果
