class Solution:
    """
    [maximum sum of numeric characters you can collect, the number of such paths that you can take to get that maximum sum]
    taken modulo 10^9 + 7.
    
    ["E23",
     "2X2",
     "12S"]
    In case there is no path, return [0, 0].
    """
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[-1, 0] for _ in range(n + 1)] for __ in range(n + 1)]
        dp[0][0], dp[n - 1][n - 1] = [0, 0], [0, 1]
        print(dp)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                for x, y in [[1, 0], [0, 1], [1, 1]]:
                    ni, nj = i + x, j + y
                    if dp[i][j][0] < dp[ni][nj][0]:
                        dp[i][j] = [dp[ni][nj][0], 0]
                    if dp[i][j][0] == dp[ni][nj][0]:
                        dp[i][j][1] += dp[ni][nj][1]
                        dp[i][j][1] %= (10**9 + 7)
                        
                if dp[i][j][0] != -1 and board[i][j] != 'E':
                    dp[i][j][0] += int(board[i][j])
                    dp[i][j][0] %= (10**9 + 7)

        return dp[0][0]
