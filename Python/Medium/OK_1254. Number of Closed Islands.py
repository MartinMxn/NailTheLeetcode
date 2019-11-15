class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        1.make all border 0 to 1 (wrong, should do dfs for each border 0)
        2.start from inner 0, mark as -1, dfs for all connect 0
        """
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        res = 0
        
        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j]==0:
                grid[i][j] = 1
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)
                
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    dfs(i, j)
                
        
        # print(grid)
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)
        
        return res
                
