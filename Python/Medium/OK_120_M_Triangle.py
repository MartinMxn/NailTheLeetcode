"""
[
     [2],       2
    [3,4],     5 6
   [6,5,0],   0 1 2
  [4,1,8,3]  0 1 2 3
]
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # O(n) n->rows
#         pre = []
#         for i, cur in enumerate(triangle):
#             if pre:
#                 for j, v in enumerate(cur):
#                     if j == 0:
#                         cur[j] += pre[j]
#                     elif j == len(cur) - 1:
#                         cur[j] += pre[len(pre) - 1]
#                     else:
#                         cur[j] += min(pre[j], pre[j - 1])
#             pre = cur
        
#         min_v = float('inf')
#         for v in cur:
#             min_v = min(min_v, v)
#         return min_v
        
        # O(n) n->rows
        # take the triangle space instead of init a tmp list
        if not triangle:
            return 0
        
        for i in range(len(triangle) - 2, -1, -1):
            for j, v in enumerate(triangle[i]):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
                
        return triangle[0][0]
        
            
