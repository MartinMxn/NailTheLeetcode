from functools import lru_cache
class Solution:
    """
    dp[i][j] = cost that needed to change first i char to j group
    dp[i][k] = min{dp[j][k - 1] + cost[j+1, i]} j from 0 to i
                and
                cost[j+1,i] -> two pointer to check palindrome
    and dp[i][j]
    """
    def palindromePartition(self, s: str, k: int) -> int:
        if len(s) <= k: return 0
        
        @lru_cache(None)
        def num_change(i, j):
            res = 0
            while i < j:
                if s[i] != s[j]: 
                    res += 1
                i += 1
                j -= 1
            return res 
        
        def dp(start, k):
            if (start, k) in memo: 
                return memo[(start, k)]
            memo[(start, k)] = math.inf
            if k == 0:
                return memo[(start, k)]
            if k == 1:
                memo[(start, k)] = num_change(start, len(s) - 1)
            for i in range(start, len(s)):
                memo[(start, k)] = min(memo[(start, k)], dp(i + 1, k - 1) + num_change(start, i))
            
            return memo[(start, k)]
        
        memo = {}
        return dp(0, k)
