class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur = res = nums[0]
        
        for i in range(1, n):
            cur = max(nums[i], nums[i] + cur)
            res = max(res, cur)
        
        return res
