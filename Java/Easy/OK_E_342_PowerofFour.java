// 4 -> 100
//right shift 2 bit each time
class Solution {
    public boolean isPowerOfFour(int num) {
        if(num < 1) return false;
        if(num == 1) return true;
        while( (num & 3) == 0 ) {   //if last three is 100
            num >>= 2;
        }
        return num == 1;
    }
}
