class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        # how to start?
        # since Each node has labels in the set {0, 1, ..., edges.length}
        # so could start from 0
        
        res = 0
        def dfs(node, pre):
            nonlocal res
            # find the 2 most larget number of it neighbors
            m1, m2 = 0, 0
            for nei in graph[node]:
                if nei != pre: # necessary since acyclic
                    dep = dfs(nei, node)
                    if dep > m1:
                        m1, m2 = dep, m1
                    elif dep > m2:
                        m2 = dep
                    res = max(res, (m1 + m2))
            return m1 + 1
            
        dfs(0, None)
        return res
