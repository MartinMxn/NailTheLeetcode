//sequence from left to right, so one step make previous * 2 is the value now from the previous bits
//add A[i] of current value
//mod by five, avoid stackoverflow
class Solution {
    public List<Boolean> prefixesDivBy5(int[] A) {
        List<Boolean> res = new ArrayList<>();
        int cur = 0;
        for(int i = 0; i < A.length; i++) {
            cur = cur * 2 + A[i];
            cur %= 5;
            res.add(cur == 0);
        }
        return res;
    }
}
