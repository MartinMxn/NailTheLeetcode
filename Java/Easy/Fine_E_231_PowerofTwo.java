/*
if n is power of 2, there will be only one 1 in the bit operation
10
100
1000
*/
class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n <= 0) return false;      
        if(n == 1) return true;
        //check whether the last one is 0, if is 0, right shift 1 until got that 1
        while( (n & 1) == 0 ){ 
            n >>= 1;
        } 
        return n == 1;
    }
}
