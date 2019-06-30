class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set((0, 0))
        h = [[-A[0][0], 0, 0]]
        m, n = len(A), len(A[0])
        res = float('inf')
        while h:
            v, x, y = heapq.heappop(h)
            res = min(res, -v)
            if (x, y) == (m - 1, n - 1):
                return res
            for di in dirs:
                nx, ny = x + di[0], y + di[1]
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(h, [-A[nx][ny], nx, ny])
                    
        return -1
