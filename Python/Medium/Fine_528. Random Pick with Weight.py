import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        """
        find the index at pre_sum array
        [1,3]
        [1,4]
        so 2 3 4 will all be 4
        
        with bisect_left
        """
        self.pre_sum_weight = []
        for wt in w:
            if self.pre_sum_weight:
                self.pre_sum_weight.append(self.pre_sum_weight[-1] + wt)
            else:
                self.pre_sum_weight.append(wt)
        
    def pickIndex(self) -> int:
        random_i = random.randint(1, self.pre_sum_weight[-1])
        # ind = bisect.bisect_left(self.pre_sum_weight, random_i)
        # return ind
    
        l, r = 0, len(self.pre_sum_weight) - 1
        while l < r:
            mid = (l + r) // 2
            if random_i > self.pre_sum_weight[mid]:
                l = mid + 1
            else:
                r = mid
        return l
        
