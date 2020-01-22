class Solution:
    """
    dfs to find all connected network, cound the extra line and compare with number of isolated node
    """
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        g = [set() for _ in range(n)]
        for a, b in connections:
            g[a].add(b)
            g[b].add(a)
        
        # count more lines and comapre
        count = 0
        visited = set()
        
        def dfs(i):
            visited.add(i)
            for nei in g[i]:
                if nei not in visited:
                    dfs(nei)
                    
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count - 1
        
