/*
determine the number of bits you would need to flip
to convert integer A to integer B
Input 29(11101), 15(01111)
Output 2
*/
class Solution {
    public int numOfFlip(int a, int b) {
        int count = 0;
//        while(a != 0 || b != 0) {
//            if(a == 0 && b != 0) {
//                int add = 0;
//                while(b != 0) {
//                    add++;
//                    b >>>= 1;
//                }
//                count += add;
//                break;
//            }
//            if(b == 0 && a != 0) {
//                int add = 0;
//                while(a != 0) {
//                    add++;
//                    a >>>= 1;
//                }
//                count += add;
//                break;
//            }
//            if(((a & 1) ^ (b & 1)) == 1 ) count++;
//            a >>>= 1;
//            b >>>= 1;
//        }

        for(int c = a ^ b; c != 0; c >>>= 1) {
            if( (c & 1) == 1) count++;
        }
        return count;
    }
}
