// 3 -> 1 10 11
// 4 -> 100
class Solution {
    public boolean queryString(String S, int N) {
        for(int i = N; i >= 0; i--) {
            if(S.indexOf(Integer.toBinaryString(i)) == -1) return false;
        }
        return true;
    }
}
