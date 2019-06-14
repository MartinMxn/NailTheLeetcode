contiguous block of memory

# Trick in Array:
Use the array itself to reduce space complexity to 0(1). [Problem 6.1]
write values from the back. [Problem 6.2]
Instead of deleting an entry consider overwriting it. [Problem 6.5]
Be comfortable with writing code that operates on subarrays. [Problem 6.10]
#### 
Don't forget the length of an array is given by the length field,  
unlike Collections, which uses the size() method, and String, which use the length() method.
#### 
Remember APIs: asListO(moreonthislater),binarySearch(A, 641),copyOf(A),  
copyOfRange(A, 1,5), equals(A, B), fill(A, 42), find(A, 28), sort(A), sort(A,cmp), toStringO.

### Bot hArrays and Collections have binarySearch() and sort() methods
## Read the review of List, ArrayList, and Collections


## 6.2 Add one to array
```
public static List<Integer> plusOne(List<Integer> arr) {
    int n = arr.size();
    int carry = 0;
    arr.set(n - 1, arr.get(n - 1) + 1);
    for (int i = n - 1; i >= 0; i--) {
        carry += arr.get(i);
        arr.set(i, carry % 10);
        carry /= 10;
    }
    if (carry > 0) {
        arr.set(0, 0);
        arr.add(0, 1);
    }
    return arr;
}
```
