/*
data[0] determine the next n - 1 number in data[] in bit format should start with 10
197
1100 0101 -> n - 1 = 2 - 1 = 1 -> should follow 1 number start with 10
235
1110 1011 -> n - 1 = 3 - 1 = 2 -> should follow 2 number start with 10

*/
class Solution {
    public boolean validUtf8(int[] data) {
        int numOfOne = 0;
        for(int i = 0; i < data.length; i++) {
            if(numOfOne == 0) {
                int val = data[i];
                /*
                128 64 32 16 8 4 2 1 0
                start with 10, val & 1000 0000 == 0
                start with 110, val & 1110 0000 == 1100 0000
                */
                if(val >= 255) return false;
                else if( (val & 128) == 0) {   // 10xx xxxx
                    continue;
                }else if( (val & 224) == 192) {   // 110x xxxx
                    numOfOne = 1;
                }else if( (val & 240) == 224) {   // 1110 xxxx
                    numOfOne = 2;
                }else if( (val & 248) == 240) {   // 1111 0xxx
                    numOfOne = 3;
                }else {
                    return false;
                }
            } else {
                if( (data[i] & 192) == 128 ){   //start with 10xx xxxx
                    numOfOne--;
                }else {
                    return false;
                }
            }
        }
        return numOfOne == 0 ? true : false;
    }
}
