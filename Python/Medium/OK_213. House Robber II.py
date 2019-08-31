class Solution:
    """
    [A,B,C,D,E]
    rob 1st and not last: nums[:-1]
    rob last but not rob 1st: num[1:]
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        if n <= 2:
            return max(nums)
        
        def rob_ori(nums):
            pre_r, pre_nr = 0, 0
            for i in range(len(nums)):
                tmp_r = pre_r
                pre_r = pre_nr + nums[i]
                pre_nr = max(pre_nr, tmp_r)
            return max(pre_r, pre_nr)
        
        return max(rob_ori(nums[:-1]), rob_ori(nums[1:]))
