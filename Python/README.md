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

## map
整体对数组元素操作
```
negative:
a = [1,2,3]
list(map(lambda x:-x, a))
[-1, -2, -3]

convert
a = ['1', '2', '3']
map(int, a)
[1, 2, 3]
```

## filter
```
>>> l = [1,2,3,4]
>>> list(filter(lambda x: x % 2 == 0, l))
[2, 4]
```

## zip/zip(*)
```
a = [1,2,3]
b = ['a', 'b', 'c']
>>> for i in zip(a,b):
...     print(i)
(1, 'a')
(2, 'b')
(3, 'c')
make it a dict
>>> dict(zip(a, b))
{1: 'a', 2: 'b', 3: 'c'}
dict.item() / for key in dict

* to decode
>>> for i in zip(*zip(a,b)):
      print(i)
(1, 2, 3)
('a', 'b', 'c')
```

## List
```
.append() # at last, equals to a[len(a):] = [x]
.pop(x) # pop last and get / any index
.extend(iterable) # 在末尾添加扩展可迭代对象 a[len(a):] = iterable
.remove() # find and delete, if not, throw ValueError
.clear()
.index(x[, start[, end]]) # return index, could have start and end, but still return from 0
.count(x)
.sort()
.reverse()
.copy()

convert to queue
collections.deque(list) convert to deque

last index
list[-1]

copy
a = b[:]
```

## deque
```
from collections import deque
append()
appendleft()
clear() / count(x) 计算x出现次数 / copy()
pop()
popleft()
```

## Set
返回一个新的 set 或 frozenset 对象，其元素来自于 iterable。 集合的元素必须为 **hashable。** ?  
无序，不重复序列
```
Creation: 
1.set1 = {"1", "2"} s = {(1,2),(2,3)}
不能用s = {}创建空set因为创建的是字典
1.1 用list创建b=set(['y', 'b', 'o','o'])
>>> b = set(['a', 'b'])
>>> b
{'b', 'a'}
1.2 利用dict创建，将会使用dict中的key值作为set的值
>>> c = set({'a1':'a', 'b2':'b'})
>>> c
{'a1', 'b2'}
1.3 使用tuple创建
>>> e={('k1', 'k2'), ('k1', 'k2')}
>>> e
{('k1', 'k2')}

2.convert from list 
  list1 = ["1", "2", "2", "1"]
  set2 = set(list1)
3.s = set()

String in set
>>> a = set("boy")
>>> a
{'y', 'o', 'b'}

更新（增加）
update
se = {11, 22, 33}
be = {22,44,55}
se.update(be)  # 把se和be合并，得出的值覆盖se
print(se) {33, 22, 55, 11, 44}
se.update([66, 77])  # 可增加迭代项
print(se) {33, 66, 22, 55, 11, 44, 77}

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

## Sort
implement by timsort  
最好情况为O(n)，平均情况为O(nlogn)，最差情况为O(nlogn)；空间复杂度为O(n)。  
derive from merge sort and insertion sort  
code is more than 1200 lines of code  
```
word = ["bca","a","b","ba",,"bda","bdca"]
word.sort(key = len)

for i in sorted(word, key = len):
  ...

for tuple, python will compare the first element in each tuple and then second...
but in this case:
item = [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
# not works
sort_items = sorted(items, key=lambda x: x.lower() if isinstance(x, str) else x)

# not works either
def get_key(x):
  print(type(x)) # tuple
  return x.lower() if isinstance(x, str) else x
sort_items = sorted(items, key=get_key)

so should be like
def get_key(x):
  return (x[0], x[1].lower())
or
sort_items = sorted(items, key=lambda x: (x[0], x[1].lower()))

```

## bisect
binary search implement
```
bisect.bisect_left(a, x, lo=0, hi=len(a))
If x is already present in a, the insertion point will be before (to the left of) any existing entries

bisect and bisect_right(a, x, lo=0, hi=len(a))
If x is already present in a, insert after the entries

insort_left same as bisect_left but also insert the x
insort_right same thing
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

## itertools
### permutation
itertools.permutations(iterable, r=None)
r为permutation每一个结果的长度
```
from itertools import *
for j in permutations([1,2,3]):
        print(j)
    '''
    (1, 2, 3)
    (1, 3, 2)
    (2, 1, 3)
    (2, 3, 1)
    (3, 1, 2)
    (3, 2, 1)
    '''
    
# permutations('ABCD', 2)
# AB AC AD BA BC BD CA CB CD DA DB DC
```
### combinations()
permutations(iterable, r) r必须
r-length tuples, in sorted order, no repeated elements
```
>>> for j in combinations([1,2,3,4], 2):
...     print(j)
... 
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)

>>> for j in combinations([1,2,3,4], 3):
...     print(j)
... 
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
(2, 3, 4)
```
### product
返回A和B中的元素组成的笛卡尔积的元组
```
>>> l1 = [1,2,3]
>>> l2 = [2,3,4]
>>> for i in product(l1, l2):
...     print(i)
... 
(1, 2)
(1, 3)
(1, 4)
(2, 2)
(2, 3)
(2, 4)
(3, 2)
(3, 3)
(3, 4)
```
### accumulate
返回可迭代序列的累加值
数字类型相加，字符类型则附加
```
a = 'abc'
b = itertools.accumulate(a)
print(list(b))
a ab abc
应用: 寻找子序列
>>> def sub(s):
       if len(s) == 1:
          return [s]
       else:
          return list(itertools.accumulate(s)) + sub(s[1:])
a ab abc b bc c
```
