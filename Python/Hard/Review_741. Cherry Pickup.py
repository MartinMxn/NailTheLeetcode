class Solution:
    """
    分别走两次不对 原因是因为第一次的路线会影响到第二次的结果， 也就是局部最优不一定是全局最优。
    让两条路线一起从开始走到结尾， 然后记录当前的状态， 这样， 就可以用一个状态来记录整体的值， 那么就可以使用动态规划。 因为走两次和两条路线一起走效果上是等价的， 而且两条路线一起走还有一个好处是可以处理重叠的情况， 这样可以在计算当前状态的时候把所有的可能情况都处理了， 当前的信息是完备的。
    """
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = {}
        
        def dfs(x1, y1, x2, y2):
            # check bottom right
            if x1 == n - 1 and y1 == n - 1:
                return grid[x1][y1] if grid[x1][y1] != -1 else float('-inf')
            
            # check valid
            if x1 == n or y1 == n or x2 == n or y2 == n or grid[x1][y1] == -1 or grid[x2][y2] == -1: 
                return float("-inf")
            
            if (x1, y1, x2, y2) in memo:
                return memo[(x1, y1, x2, y2)]
            
            # cherry, if at same point, only pickup one
            # use number is fine
            if x1 == x2 and y1 == y2:
                cherry = grid[x1][y1]
            else:
                cherry = grid[x1][y1] + grid[x2][y2]
            
            res = cherry + max(
                dfs(x1 + 1, y1, x2 + 1, y2), 
                dfs(x1, y1 + 1, x2, y2 + 1),
                dfs(x1 + 1, y1, x2, y2 + 1),
                dfs(x1, y1 + 1, x2 + 1, y2),
            )
            
            memo[(x1, y1, x2, y2)] = res #! need memo
            return res
                
        ans = dfs(0, 0, 0, 0)
        return ans if ans != float('-inf') else 0
