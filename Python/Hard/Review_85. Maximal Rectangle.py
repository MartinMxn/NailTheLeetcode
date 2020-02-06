class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        using #84 histogram idea
             10100 means at idx 0, 2 is rectangle histogram
        then 10111 means 2,0,2,1,1
        """
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        columns_height = [0] * m
        res = 0
        for i in range(n):
            
            for j in range(m):
                if matrix[i][j] == '1':
                    columns_height[j] += 1
                else:
                    columns_height[j] = 0
            # then do #84 for each round
            res = max(res, self.largestRectangleArea(columns_height))
        
        return res
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monolithic stack
        # always remember the increase heights before idx
        # stack store the idx, not the value
        stack = [-1]
        res = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and h < heights[stack[-1]]:
                prev_i = stack.pop()
                prev_h = heights[prev_i]  # prev_h is always smaller than previous pop heights, so could use prev_h as max height
                # like 5,6,2 when at 2, calculate 6, then 5, then 2 outside of for loop
                width = i - 1 - stack[-1]
                res = max(res, width * prev_h)
                
            stack.append(i)
        
        while stack[-1] != -1:
            prev_i = stack.pop()
            prev_h = heights[prev_i]
            width = len(heights) - stack[-1] - 1 # dif with for loop, stack[-1] is the prev idx after pop
            res = max(res, width * prev_h)
            
        return res
