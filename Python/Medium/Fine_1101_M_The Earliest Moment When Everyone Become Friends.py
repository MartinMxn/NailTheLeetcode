class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        uf = {x: x for x in range(N)}
        self.groups = N
        
        def union(x, y):
            nx, ny = find(x), find(y)
            if nx != ny:
                self.groups -= 1
                uf[nx] = ny
            
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        for t, x, y in sorted(logs):
            union(x, y)
            if self.groups == 1:
                return t
            
        return -1
