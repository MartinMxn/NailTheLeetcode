## Math module
provides access to the mathematical functions defined by the C standard.  
####
cannot be used with complex numbers;  
use the functions of the same name from the cmath module if you require support for complex numbers. 

除特殊标注一般都return float类型
```
math
  .ceil(x)
  .floor(x)
  .copysign(x, y)
Return a float with the magnitude (absolute value) of x but the sign of y.  
On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.

  .fabs(x) # not abs
Return the absolute value of x.

  .factorial(x)
Return x factorial as an integer. Raises ValueError if x is not integral or is negative.

  .fmod(x, y)
  .fsum(iterable)
  .gcd(a, b)
Return the greatest common divisor of the integers a and b.  
If either a or b is nonzero, then the value of gcd(a, b) is the largest positive integer that divides both a and b. gcd(0, 0) returns 0.
  
  .isfinite(x)
Return True if x is neither an infinity nor a NaN, and False otherwise.

  .log(x[, base])
With one argument, return the natural logarithm of x (to base e).
With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).

  .log2(x)
Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).

  .log10(x)同上
  .pow(x, y)
Unlike the built-in ** operator, math.pow() converts both its arguments to type float. 
Use ** or the built-in pow() function for computing exact integer powers.

  .sqrt(x)
  .math.pi
  .math.e
  .math.inf
A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf').

  .math.nan
A floating-point “not a number” (NaN) value. Equivalent to the output of float('nan').
```
