class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_sum = 0
        table = {0: 0}
        res = 0
        # second parameter in enumerate, is from where to start the index.
        for i, v in enumerate(nums, 1):
            if v == 0:
                pre_sum -= 1
            else:
                pre_sum += 1
            
            if pre_sum not in table:
                table[pre_sum] = i
            else:
                res = max(res, i - table[pre_sum])
            
        return res
            
