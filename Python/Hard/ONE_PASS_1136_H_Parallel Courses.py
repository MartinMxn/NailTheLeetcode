class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        degree = {i: 0 for i in range(1, N + 1)}
        out = collections.defaultdict(set)

        for i, j in relations:
            out[i].add(j)
            degree[j] += 1
            
        # add all in-degree 0 node to graph
        visited = set()
        q = collections.deque()
        for n in degree:
            if degree[n] == 0:
                q.append(n)
        
        step = 0
        # bfs topo traverse
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                for o in out[cur]:
                    if o not in visited:
                        visited.add(o)
                    degree[o] -= 1
                    if degree[o] == 0:
                        q.append(o)
            step += 1
            
        if len(visited) == N:
            return step
        
        return -1
