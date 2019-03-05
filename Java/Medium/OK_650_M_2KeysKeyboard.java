class Solution {
    public int minSteps(int n) {
//         int[] dp = new int[n + 1];
        //first one don't need to copy/paste, so from 2
//         for(int i = 2; i <= n; i++) {
//             for(int j = i / 2; j > 0; j--) {
//                 //from i / 2, if i % j == 0, we just need to copy+paste/paste/paste... i / j steps
//                 if(i % j == 0) {
//                     dp[i] = dp[j] + i / j;
//                     break;
//                 }
//             }
//         }
//         return dp[n];
        
        //i 'A' could be achieve by dp[j] + i / j
        //copy itself and past i / j - 1 times
        //1 + i/j -1 = i / j
        int[] dp = new int[n + 1];
        for(int i = 2; i <= n; i++) {
            for(int j = i / 2; j >= 1; j--) {
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
