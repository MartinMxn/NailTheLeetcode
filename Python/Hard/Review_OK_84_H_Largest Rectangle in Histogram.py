class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force TLE
        # find the min height for every height
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
        """
        maintain a monolithic stack to store index
        the height of the index we store in stack is always increasing
        because:
                  6 
                5
            
                      3
            2       2
              1     
            0 1 2 3 4 5
        from the period 1 5 6, if we calculate the height from 6 to 5 to 1 the height after 5 and 1
        are always height than themself, so we just care about width
        
        if we meet decrease, we could just pop and calculate the higher height, 
        the left stack are all increase, and calculate them at the end
        """
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
            print(stack)
            while stack[-1] != -1:
                prev_i = stack.pop()
                prev_h = heights[prev_i]
                width = len(heights) - stack[-1] - 1 # dif with for loop, stack[-1] is the prev idx after pop
                res = max(res, width * prev_h)

            return res
