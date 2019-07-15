class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}
        res = 0
        pre_sum = 0
        for i, v in enumerate(nums):
            va = 1 if v == 1 else -1
            pre_sum += va
            if pre_sum in mp:
                res = max(res, i - mp[pre_sum])
            else:
                mp[pre_sum] = i
        return res
