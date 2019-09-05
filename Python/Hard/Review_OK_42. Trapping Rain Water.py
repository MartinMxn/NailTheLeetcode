class Solution:
    """
    for the largest water, we need to find the largest bot
    the area is min(height[left], height[right])
    
    look at the decrease sequence
    
       
      2       2
        1   1
          0
      0 1 2 3 4 5 6
    if still decrease, we can't hold water
    but once we find the height increase, we could calculate the area by keep poping the index in stack
    each time is the height of current index, width is i - cur_i, cause we know the i is must lower than cur_i
    """
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()
                if stack:
                    min_h = min(height[stack[-1]], h)
                    width = i - stack[-1] - 1
                    water_h = min_h - height[bottom]
                    res += water_h * width
            stack.append(i)
        
        return res
        
