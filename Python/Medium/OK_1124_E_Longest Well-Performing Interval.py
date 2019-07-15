class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        mp = {}
        pre_sum = 0
        res = 0
        for i, v in enumerate(hours):
            cur = 1 if v > 8 else -1
            pre_sum += cur
            
            # if pre_sum > 0, the range from 0 to i is longest
            if pre_sum > 0:
                res = i + 1
            elif pre_sum - 1 in mp:
                res = max(res, i - mp[pre_sum - 1])
                
            if pre_sum not in mp:
                mp[pre_sum] = i
        return res
