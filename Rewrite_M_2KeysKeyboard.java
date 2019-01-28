public class Rewrite_M_2KeysKeyboard {

    // public int minSteps(int n) {
    //     int[] dp = new int[n + 1];
    //     for(int i = 2; i <= n; i++){
    //         for(int j = i / 2; j > 0; j--){
    //             if(i % j == 0){
    //                 dp[i] = dp[j] + i / j;
    //                 break;
    //             }
    //         }
    //     }
    //     return dp[n];
    // }

    //no extra dp
    //the res is quotient of target number divided by the first factor
    public int minSteps(int n) {
        if(n == 1) return 0;
        for(int i = 2; i < n; i++){
            if(n % i == 0){
                return i + minSteps(n / i);
            }
        }
        return n;
    }
}
