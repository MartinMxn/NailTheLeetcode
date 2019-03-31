//former best one decrease 1 each step, calculate it as constant number compared with A[i]
//and store as cur
//calculate sum
class Solution {
    public int maxScoreSightseeingPair(int[] A) {
        int res = 0, cur = 0;
        for(int i = 0; i < A.length; i++) {
            res = Math.max(res, cur + A[i]);
            cur = Math.max(cur, A[i]) - 1;
        }
        return res;
    }
}
