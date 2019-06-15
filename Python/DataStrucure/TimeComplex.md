## list
``` 
Operation              Efficiency
index:      a[i]         O(1)
assignment a[i]=1        O(1)
append    a.append(1)    O(1)
pop()      a.pop()       O(1)

pop(i)     a.pop(3)      O(n)
insert  a.insert(1, v)   O(n)
del        del           O(n)
iteration                O(n)
contains   1 in a        O(n)
get slice   a[x:y]       O(k) k = y - x - 1
del slice  del a[x:y]    O(n)
! set slice   a[x:y] = [z,...]  O(n + k) n = original length, k = new length

a = [0,1,2,3,4]
# make 1 - 2 to 8,9,10
a[1:3] = [8,9,10]
print(a)
# [0, 8, 9, 10, 3, 4]

reverse                  O(n)
concatenate              O(k) k = new list length
sort                     O(nlogn)
! multiply  a = [1]*10   O(nk)

```

## dict
```
Operation              Efficiency
copy/iteration:          O(n)
get/set/del/contains     O(1)
```
### In Python, l1 = l1 + [i]  != l1 += [i]
+= is better, add new list at the end of original list  
however, = create a new list and add both, point the l to this new list, so is worse

## ADT
抽象数据类型(ADT)的含义是指一个数学模型以及定义在此数学模型上的一组操作。
```
class Student(obj):
  def add(self):
  def pop(self):
```
