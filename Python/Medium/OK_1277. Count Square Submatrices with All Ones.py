class Solution:
    """
    classic dp, dp[i][j] is the i, j point as bottom right point of square
    
    current status can be come from dp[i-1][j], dp[i-1][j-1], dp[i][j-1]
    because dp[i - 1][j] take care of the rectangle which bottom right is i - 1,j, 
    dp[i-1][j-1] and dp[i][j-1] is same idea
    if any of them is smaller, then the count only add 1 based on the smallest one

    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    """
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
        res = 0
        
        for i in range(1, n + 1): # careful for n + 1, not n
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                res += dp[i][j]
        
        return res
