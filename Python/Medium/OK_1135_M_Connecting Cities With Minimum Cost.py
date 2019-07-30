class Solution:
    '''
    sort based on cost
    add if not a union
    check the number of group
    '''
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        uf = {}
        res = 0
        count = N
        
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            uf[find(x)] = find(y)
        
        for x, y, cost in sorted(connections, key=lambda x: x[2]):
            if find(x) != find(y):
                union(x, y)
                res += cost
                N -= 1
        
        return res if N == 1 else -1
        
