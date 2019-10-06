class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(n + 1):
            dp[i][0] = i
            
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[n - j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        # print(dp)
        return dp[-1][-1] <= k * 2
