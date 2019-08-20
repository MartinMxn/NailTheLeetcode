class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # find the start/end point and number of 0
        n, m = len(grid), len(grid[0])
        
        def neighbors(i, j):
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] in (0, 2):
                    yield ni, nj
        
        num_ob = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1: num_ob += 1
                if grid[i][j] == 1: si, sj = i, j
                if grid[i][j] == 2: ei, ej = i, j    
        
        self.ans = 0
        def dfs(i, j, num_ob):
            num_ob -= 1
            if num_ob < 0: return
            if i == ei and j == ej: # seperate two if since once we get to end, we should stop no matter wether go through all 0
                if num_ob == 0:
                    self.ans += 1
                return
                
            grid[i][j] = -1
            # for dirs
            for ni, nj in neighbors(i, j):
                dfs(ni, nj, num_ob)
        
            grid[i][j] = 0
        
        dfs(si, sj, num_ob)
        return self.ans
