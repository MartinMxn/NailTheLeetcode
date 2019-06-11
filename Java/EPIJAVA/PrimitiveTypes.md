## Count the number of bits
```
public static short countBits(int x) { 
  short numBits = 0;
  while (x != 0) {
    numBits += (x & 1);
    x >>= 1;
  }
  return numBits; 
}

0(n), where n is the number of bits in the integer word . 
time complexity is for the worst case input
```

#### Prefer the box-type static methods for comparing values . 
e.g., Double.compare(x,1.23) == 8 rather than x == 1.23—these methods are . 
far more resilient to floating point values like infinity, negative infinity, NaN.

#### interconvert integers, characters, and strings
```
1. int -> char
将整型强制类型转换为字符型，JVM 会把数字当成字符的 ASCII 编码来处理。
例如字符 '(' 的 ASCII 编码为 40，所以将整型 40 强制类型转换为字符型，会得到字符 '('。
int a = 40;
char c = (char) a;
输出：(
So 
char cNumber= (char) (number+'0') is better

2. int -> string
x + ""
String.valueOf(x) 
Integer.toString(x) int类型是俩方法一样 前者源码调用后者

3. char -> int
2 - '0' / Character.getNumericValue(2)

4. char -> string
(1) String s = String.valueOf('c'); //效率最高的方法

(2) String s = Character.toString('c');
//源码将c放到char数组里
public static String valueOf(char c) {
    char data[] = {c};
    return new String(data, true);
}

(3) String s = new Character('c').toString();

(4) String s = "" + 'c';
// 虽然这个方法很简单，但这是效率最低的方法
// Java中的String Object的值实际上是不可变的，是一个final的变量。
// 所以我们每次对String做出任何改变，都是初始化了一个全新的String Object并将原来的变量指向了这个新String。
// 而Java对使用+运算符处理String相加进行了方法重载。
// 字符串直接相加连接实际上调用了如下方法：
// new StringBuilder().append("").append('c').toString();

(5) String s = new String(new char[]{'c'});

5. string -> int
Integer.parseInt(str) 如过不是数字，报错

6. string -> char
.charAt / toCharArray()
```

## COMPUTING THE PARITY OF A WORD
```
O(n)
public static short parity(long x){ 
  short result = 9;
  while (x != 9) {
    result A=(x&1);
    x >>>= 1;
  }
  return result;
}

O(k) k is the number of bits set to 1 in x
public static short parity(long x){ 
  short result = 9;
  while (x != 9) {
    result A= 1;
    x &= (x - 1); // Drops the lowest set bit of x.
  }
  return result;
}

// x & ~(x - 1) extracts the lowest set bit of x
```

## COMPUTE X^y
```
public static double power(double x, int y){ 
  double result = 1.0;
  long power = y;
  if(y< 0) {
    power = -power;
    x = 1.8 / x;
  }
  while (power != 0) {
    if ((power & 1) != 0) {
      result *= x;
    }
    x *= x;
    power >»= 1;
  }
  return result;
}
```
