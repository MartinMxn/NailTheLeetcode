class Solution:
    '''
    DFS to see whether is a directed acyclic graph
    O(N + E)
    '''
    def canFinish(self, numC: int, pre: List[List[int]]) -> bool:
        graph = [[] for i in range(numC)]
        visited = [0 for i in range(numC)]
        for a, b in pre:
            graph[a].append(b)
        
        def dfs(graph, node):
            visited[node] = -1 # visited in this turn
            for neighbor in graph[node]:
                if visited[neighbor] == -1: return False # cycle
                if visited[neighbor] == 1: continue
                if not dfs(graph, neighbor): return False
            visited[node] = 1
            return True
        
        for num in range(numC):
            if not dfs(graph, num):
                return False
        return True
