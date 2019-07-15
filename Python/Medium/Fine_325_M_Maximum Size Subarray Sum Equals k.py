class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """
        map to store the current num first appeared position
        if pre_sum - k in mp, [pre_sum - k + 1, i] is possible ans, and update res
        """
        mp = {0: -1} # if pre sum + cur value = k, pre sum - k = 0
        res = 0
        pre_sum = 0
        for i, v in enumerate(nums):
            pre_sum += v
            if pre_sum not in mp:
                mp[pre_sum] = i
            if pre_sum - k in mp:
                res = max(res, i - mp[pre_sum - k])
        return res
