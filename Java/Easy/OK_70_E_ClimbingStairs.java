/*
! from 3
each step we could 1 or 2
so to height n, we could from n - 1 / n - 2
and res at height n should be dp[n - 1] + dp[n - 2]
*/
class OK_70_E_ClimbingStairs {
    public int climbStairs(int n) {
        if(n <= 2) return n;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for(int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}
