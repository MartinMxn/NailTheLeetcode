"""
follow up: print the final graph with water 'w'
"""
class Solution:
    """
    After V units of water fall at index K, how much water is at each index?
    """
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        n = len(heights)
        def drop(heights, k):
            drop_loc = k
            for i in range(-1, 2, 2):
                cur = k + i
                while cur >= 0 and cur < n and heights[cur] <= heights[cur - i]:
                    if heights[cur] < heights[drop_loc]:
                        drop_loc = cur
                    cur += i
                if drop_loc != k:
                    break
            # already find the position
            heights[drop_loc] += 1
        
        while V > 0:
            drop(heights, K)
            V -= 1
        
        return heights
