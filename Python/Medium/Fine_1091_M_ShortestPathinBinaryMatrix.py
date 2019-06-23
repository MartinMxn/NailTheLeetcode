class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        bfs to check 8 directions
        no need to dp, bfs makes the shortest turn
        """
        n = len(grid)
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        count = 1
        bfs = [[0,0]]
        seen = {(0,0)}
        
        def nei(i, j):
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if 0<=i+di<n and 0<=j+dj<n:
                        yield (i + di, j + dj)
            
        while bfs:
            count += 1
            tmp_bfs = []
            for i, j in bfs:
                for x, y in nei(i, j):
                    if grid[x][y] != 1 and (x, y) not in seen:
                        tmp_bfs.append([x, y])
                        seen.add((x, y))
                    if (x, y) == (n - 1, n - 1):
                        return count
            bfs = tmp_bfs
            
        return -1
                    1091. Shortest Path in Binary Matrix
