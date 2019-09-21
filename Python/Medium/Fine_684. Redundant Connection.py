class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        dfs to find the cycle edges
        O(n^2)
        """
#         graph = collections.defaultdict(set)
#         # set to make no repeat
        
        
#         def dfs(start, end):
#             for to in graph[start]:
#                 if to == end:
#                     return True
#                 elif to not in seen:
#                     seen.add(to)
#                     return any(dfs(to, end) for nei in graph[to])
        
#         for i, j in edges:
#             seen = set()
#             if i in graph and j in graph and dfs(i, j):
#                 return i, j
                
#             graph[i].add(j)
#             graph[j].add(i)
        
        """
        union find O(nlogn - n)
        """
        uf = [i for i in range(len(edges))]
        
        def find(x):
            if uf[x] != x:
                return find(uf[x])
            else:
                return x
        
        def union(x, y):
            # print(x, y)
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            uf[rootX] = rootY
            # print(uf)
            return True
        
        for i, j in edges:
            if not union(i - 1, j - 1):
                return i, j
        
        raise ValueError("Illegal input")
        
        
