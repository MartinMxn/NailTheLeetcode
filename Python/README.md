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
```

## List
```
.append() # at last
.pop() # pop last and get
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
