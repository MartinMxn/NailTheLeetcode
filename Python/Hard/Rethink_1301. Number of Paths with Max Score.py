class Solution:
    # 3d dp
    # dp[i][j][0], max sum of path
    # dp[i][j][1], number of such path
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        if not board or not board[0]:
            return [0, 0]
        
        n, mod = len(board), 10**9 + 7
        dp = [[[-1, 0] for _ in range(n + 1)] for __ in range(n + 1)]
        dp[0][0] = [0, 0]
        dp[n - 1][n - 1] = [0, 1]
        
        for i in range(n)[::-1]:
            for j in range(n)[::-1]:
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue
                for x, y in [[0, 1], [1, 0], [1, 1]]:
                    nx, ny = i + x, j + y
                    if dp[i][j][0] < dp[nx][ny][0]:
                        dp[i][j] = [dp[nx][ny][0], 0]
                    if dp[i][j][0] == dp[nx][ny][0]: # if equal, add the number of nx, ny cell
                        dp[i][j][1] += dp[nx][ny][1]
                        dp[i][j][1] %= mod
                
                # if there exits some path from 'E' to current position, update info of current position
                if dp[i][j][0] != -1 and (i or j):
                    dp[i][j][0] += int(board[i][j])
                    dp[i][j][0] %= mod
                    
        return dp[0][0]
