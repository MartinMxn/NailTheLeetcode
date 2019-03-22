/*
start from result and binary search
*/
class Solution {
    public int shipWithinDays(int[] weights, int D) {
        int left = 0, right = 0;
        for(int i : weights) {
            left = Math.max(left, i);
            right += i;
        }
        //binary search
        while(left < right) {
            int mid = left + (right - left) / 2;
            int need = 1, cur = 0;
            for(int i : weights) {
                if(cur + i > mid) {
                    need++;
                    cur = 0;
                }
                cur += i;
            }
            if(need > D) left = mid + 1;
            else right = mid;
        }
        return left;
    }
}
