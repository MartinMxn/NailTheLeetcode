//think from how to convert to 2 base
//then -2 base diff is odd position bit
class Solution {
    public String baseNeg2(int N) {
        if(N == 0) return Integer.toString(N);
        StringBuilder sb = new StringBuilder();
        while(N != 0) {
            sb.append(Integer.toString(N & 1));
            N = -(N >> 1);
        }
        return sb.reverse().toString();
    }
}
