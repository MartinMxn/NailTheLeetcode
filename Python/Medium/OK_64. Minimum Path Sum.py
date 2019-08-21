class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # if we could modify the original grid
        # take the original 2d grid as dp
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i != 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]
