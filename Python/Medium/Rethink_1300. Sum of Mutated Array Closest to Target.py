class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # the value need to return, will make all the number in arr that 
        # larger than value change to value, then the sum of arr will closest to target
        # value may not be the number in arr
        
        """
        the ans must be in [0, max(arr)]
        so for each time we take a guess, we could calculate the sum and compare with target
        and tmp
        """
        
        l, r = 0, max(arr)
        sub, res = float('inf'), float('inf')
        
        while l <= r:
            mid = (l + r) // 2
            
            tmp_sum = 0
            for num in arr:
                if num > mid:
                    tmp_sum += mid
                else:
                    tmp_sum += num
            
            cur_sub = abs(tmp_sum - target) #当前差的最小值
 
            if cur_sub < sub: # 如果有更小的答案
                sub = cur_sub
                res = mid
            elif cur_sub == sub:
                res = min(res, mid)
            
            if tmp_sum > target:
                r = mid - 1
            elif tmp_sum < target:
                l = mid + 1
            else:
                return mid
            
        return res
