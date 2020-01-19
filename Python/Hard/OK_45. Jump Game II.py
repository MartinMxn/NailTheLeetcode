# 2 with jump game
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        mx = [0 for _ in range(n + 1)]
        
        # update to jump game II format
        for i, d in enumerate(ranges):
            left, right = max(0, i - d), min(n, d + i)
            mx[left] = max(mx[left], right - left)
        
        step, far, curend = 0, 0, 0
        for i in range(n):
            far = max(far, mx[i] + i)
            if i > curend:
                return -1
            if i == curend:
                curend = far
                step += 1
        
        return step
# 1
class Solution:
    """
    minimize the step we waste
    update curend to make sure we take furtherest
    when i == curend, update this period far by curfat
    when between, update curfar every time
    """
    def jump(self, nums: List[int]) -> int:
        step, curend, far = 0, 0, 0
        for i in range(len(nums) - 1):
            far = max(far, nums[i] + i)
            if i == curend:
                curend = far
                step += 1
        
        return step
