"""
[1  3  -1] -3  5  3  6  7       3
 0
 1  2
 1 [3  -1  -3] 5  3  6  7       3
    res = [3]
    start = 1, end = 3
    
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        
        dq = collections.deque()
        
        def add_to_deque(dq, nums, index):
            while len(dq) and nums[dq[-1]] <= nums[index]:
                dq.pop()
            dq.append(index)
            
        # init dq
        res = []
        start, end = 0, k - 1
        for i in range(k):
            add_to_deque(dq, nums, i)
            
        while end < len(nums):
            while True:
                if dq[0] >= start:
                    res.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()
            start, end = start + 1, end + 1
            if end < len(nums):
                add_to_deque(dq, nums, end)
        
        return res
        
