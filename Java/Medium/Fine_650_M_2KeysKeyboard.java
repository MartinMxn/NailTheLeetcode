class Solution {
    public int minSteps(int n) {
        int[] dp = new int[n + 1];
        //first one don't need to copy/paste, so from 2
        for(int i = 2; i <= n; i++) {
            for(int j = i / 2; j > 0; j--) {
                //from i / 2, if i % j == 0, we just need to copy+paste/paste/paste... i / j steps
                if(i % j == 0) {
                    dp[i] = dp[j] + i / j;
                    break;
                }
            }
        }
        return dp[n];
    }
}  
//no extra dp
//the res is quotient of target number divided by the first factor
// public int minSteps(int n) {
//     if(n == 1) return 0;
//     for(int i = 2; i < n; i++){
//         if(n % i == 0){
//             return i + minSteps(n / i);
//         }
//     }
//     return n;
// }
