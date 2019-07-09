class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force TLE
#         if len(heights) == 0:
#             return 0
#         res = heights[0]
#         pt = 0
        
#         def check(heights, end_idx):
#             res = min_v = heights[pt]
#             for i in range(end_idx, -1, -1):
#                 min_v = min(heights[i], min_v)
#                 res = max(res, min_v * (end_idx - i + 1))
#             return res
            
#         while pt < len(heights) - 1:
#             if heights[pt + 1] < heights[pt]:
#                 max_v = check(heights, pt)
#                 res = max(max_v, res)
#             elif heights[pt + 1] == heights[pt]:
#                 max_v = check(heights, pt + 1)
#                 res = max(max_v, res)
#             pt += 1
#         res = max(res, check(heights, pt)) # check at then end, prevent all increasing case
#         return res
    
        # stack
        if not heights:
            return 0
        stack = [-1]
        res = 0
        
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                tmp_i = stack.pop()
                tmp_h = heights[tmp_i]
                res = max(res, tmp_h * (i - stack[-1] - 1) )
            stack.append(i)
        
        while stack[-1] != -1:
            tmp_i = stack.pop()
            tmp_h = heights[tmp_i]
            res = max(res, tmp_h * (len(heights) - stack[-1] - 1))
            
        return res
