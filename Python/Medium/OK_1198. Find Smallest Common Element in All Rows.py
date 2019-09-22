class Solution:
    """
    [1,2,3,4,5],
    [2,4,5,8,10],
    [3,5,7,9,11],
    [1,3,5,7,9]
    
    smallest one must in the first row, 
    so try all ele in first rot from left to right, bisect on each row
    if idx == len(max), we find it
    """
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        for e in mat[0]:
            row = 1
            found = True
            while row < n:
                p = bisect.bisect_left(mat[row], e)
                if p == n or mat[row][p] != e:
                    found = False
                    break
                else:
                    row += 1
            if row == n and found:
                return e
        
        return -1
                    
