class Solution:
    def numTrees(self, n: int) -> int:
        # select root every time
        # divide to left and right part
        # 0 ~ i - 1 and i + 1 ~ n - 1
        # i 
        
        # recursion TLE
#         if n == 0 or n == 1:
#             return 1
#         sum_v = 0
#         # sum all node result
#         for i in range(1, n + 1):
#             sum_v += self.numTrees(i - 1) * self.numTrees(n - i)
        
#         return sum_v
        
        # dp
        dp = [0 for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(1, n + 1):
            sum_v = 0
            for j in range(1, i + 1):
                sum_v += dp[j - 1] * dp[i - j]
            dp[i] = sum_v
            
        return dp[-1]
    
