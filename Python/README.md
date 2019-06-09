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
5. Reverse loop
for i in range(len(arr) - 2, -1, -1):
  ...
```

## String
#### find(str, beg=0, end=len(string))) / rfind(...)
```
find str -- 指定检索的字符串. beg -- 开始索引，默认为0. end -- 结束索引，默认为字符串的长度。
如果子序列不存在返回-1

rfind() 从右向左寻找子序列的位置
index()/rindex() same as find, but 如果子序列不存在报错，所以一般我们用find()
```

## List
```
.append() # at last
.pop() # pop last and get

index()
Return the smallest index / the first occurrence of x in the array.
Otherwise, return a ValueError.

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

## heapq
```
heappush(heap, item)：将 item 元素加入堆。
heappop(heap)：将堆中最小元素弹出。
heapify(heap)：将堆属性应用到列表上。
heapreplace(heap, x)：将堆中最小元素弹出，并将元素x 入堆。
merge(*iterables, key=None, reverse=False)：将多个有序的堆合并成一个大的有序堆，然后再输出。
heappushpop(heap, item)：将item 入堆，然后弹出并返回堆中最小的元素。
nlargest(n, iterable, key=None)：返回堆中最大的 n 个元素。
nsmallest(n, iterable, key=None)：返回堆中最小的 n 个元素。

heapq.heappush(heap, item)
    - Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap)
    - Pop and return the smallest item from the heap, maintaining the heap invariant.
    If the heap is empty, IndexError is raised. 
heap[0]
    To access the smallest item without popping it.
    
heapq有两种方式创建堆， 
1 是使用一个空列表，然后使用heapq.heappush()函数把值加入堆中
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆
    
2 使用heap.heapify(list)转换列表成为堆结构
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)

heapq.nlargest() / heapq.nsmallest() 获取堆中n个最大或最小的值
Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
>>> nums = [1, 3, 4, 5, 2]
>>> import heapq
>>> print(heapq.nlargest(2, nums))
[5, 4]
>>> print(heapq.nsmallest(2, nums))
[1, 2]

Merge two heap
num1 = [32, 3, 5, 34, 54, 23, 132]
num2 = [23, 2, 12, 656, 324, 23, 54]
num1 = sorted(num1)
num2 = sorted(num2)

res = heapq.merge(num1, num2)

heapq.heaprepalce()
删除堆中最小元素并加入一个元素
nums = [1, 2, 4, 5, 3]
heapq.heapify(nums)
heapq.heapreplace(nums, 23)
# out: [2, 3, 4, 5, 23]
```

### max heap in python
heapq.heappush(heap_name, -num)
negative of number in min heap is max heap


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
### Counter类（计数器）
用于追踪值的出现次数
Counter类继承dict类，所以它能使用dict类里面的方法 
```
import collections
obj = collections.Counter('aabbccc')
print(obj)
#输出：Counter({'c': 3, 'a': 2, 'b': 2})
```
#### most_common(指定一个参数n，列出前n个元素，不指定参数，则列出所有)
```
import collections
obj = collections.Counter('aabbbcccc')
print(obj.most_common(2))
#输出：[('c', 4), ('b', 3)]
```

#### items()
```
import collections
obj = collections.Counter('aabbbcccc')
print(obj.items())

for k,v in obj.items():
    print(k,v)

#输出：dict_items([('b', 3), ('c', 4), ('a', 2)])
#     b 3
#     c 4
#     a 2
```

#### update()/subtract()
```
update(增加元素)

import collections
obj = collections.Counter(['11','22'])
obj.update(['22','55'])
print(obj)
#输出：Counter({'22': 2, '11': 1, '55': 1})

subtract(原来的元素减去新传入的元素)

import collections
obj = collections.Counter(['11','22','33'])
obj.subtract(['22','55'])
print(obj)

#输出：Counter({'11': 1, '33': 1, '22': 0, '55': -1})
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

## yield 表达式 ??
把一个函数变成一个生成器generator
用来延迟，在需要时候再产生结果

## Trie Tree
```
class Trie:
    def __init__(self, words):
        self.trie = {}
        for word in words:
            cur = self.trie
            for c in words:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            trie["end"] = True
```
