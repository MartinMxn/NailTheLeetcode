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
