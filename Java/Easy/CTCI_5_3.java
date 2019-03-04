/*
flip one 0 to 1
find the longest length of 1 you could create
Input: 110111001
Ouput: 6
*/
class Solution {
    public int longestSeq(int n) {
        if(~n == 0) return Integer.BYTES * 8;
        int curLen = 0, preLen = 0, maxLen = 1;
        //use n as flag and logic right shift
        while(n != 0) {
            if((n & 1) == 1) {  //if cur bit is 1
                curLen++;
            } else if((n & 1) == 0) { // cur bit is 0
                //if next one is 0, like 00, so preLen = 0
                preLen = (n & 2) == 0 ? 0 :curLen;
                curLen = 0;
            }
            maxLen = Math.max(maxLen, curLen + preLen + 1);
            n >>>= 1;
        }
        return maxLen;
    }
}
//O(b) bit
//O(1)
