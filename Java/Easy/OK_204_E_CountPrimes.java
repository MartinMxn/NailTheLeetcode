//mark all profuct of prime and count the left number
class Solution {
    public int countPrimes(int n) {
        boolean[] p = new boolean[n];
        int res = 0;
        
        for (int i = 2; i < n; i++) {
            if (!p[i]) {
                res++;
                for (int j = i; j < n; j += i) {
                    p[j] = true;
                }
            }
        }
        
        return res;
    }
}
