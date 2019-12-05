class Solution:
    """
    classic dp, dp[i][j] is the i, j point as bottom right point of square
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
