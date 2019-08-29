class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #  2206 -> 22
        # 01234
        # F(n) -> first n char combinations
        # F(n) = F(n - 1) + F(n - 2) 
        # !compare with string instead of convert to number
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1 # empty string can form only one possibility
        
        for i in range(1, n + 1):
            if s[i - 1] != '0': 
                dp[i] += dp[i - 1]
            if i > 1 and s[i - 2] > '0' and s[i - 2] + s[i - 1] <= '26': 
                dp[i] += dp[i - 2]
        
        return dp[-1]
        
