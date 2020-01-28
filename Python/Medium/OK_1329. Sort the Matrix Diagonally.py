class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        
        dif = collections.defaultdict(list)

        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                dif[i - j].append(mat[i][j])
        
        for i in dif:
            dif[i].sort()
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = dif[i - j].pop(0)
                
        return mat
