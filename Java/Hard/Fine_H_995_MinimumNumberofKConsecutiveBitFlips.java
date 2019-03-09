/*
0 0 0 1 0 1 1 0
1 1 1 1 0 1 1 0
1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 1

start from first '1', cause other element may filp by the previous ones
the first one only flip by event start from itself

flip A.length - K + 1 times to flip all first A.length - K + 1 elements to 1
then check the left K - 1 element, if there's a 0, we can't do that anyway
*/
class Solution {
    public int minKBitFlips(int[] A, int K) {
        int res = 0;
        for(int i = 0; i < A.length - K + 1; i++) {
            if(A[i] == 0) {
                flipK(A, i, K);
                res++;
            }
        }
        for(int i = A.length - K; i < A.length; i++) {
            if(A[i] == 0) {
                return -1;
            }
        }
        return res;
    }
    
    private void flipK(int[] A, int start, int K) {
        for(int i = start; i < start + K; i++) {
            A[i] = (A[i] == 0) ? 1 : 0;
        }
    }
}
