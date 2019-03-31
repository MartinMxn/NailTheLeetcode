//sum up all number to see whether is a multiple of 3
//find the first part sum equal to 1/3 of sum, and second, if them exist, return true
class Solution {
    public boolean canThreePartsEqualSum(int[] A) {
        int sum = 0;
        for(int i : A) {
            sum += i;
        }
        if(sum % 3 != 0) return false;
        int tmp = 0;
        boolean first = false, second = false;
        for(int i = 0; i < A.length; i++) {
            if(tmp == sum / 3) {
                if(first) return true;
                first = true;
                tmp = 0;
            }
            tmp += A[i];
        }
        return false;
    }
}
