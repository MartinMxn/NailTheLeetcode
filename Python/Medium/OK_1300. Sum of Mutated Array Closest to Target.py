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
        dif, res = float('inf'), float('inf')
        
        while l <= r:
            mid = (r + l) // 2
            cur_sum = 0
            for num in arr:
                if num < mid:
                    cur_sum += num
                else:
                    cur_sum += mid
            
            cur_dif = abs(cur_sum - target)
            if cur_dif < dif:
                dif = cur_dif
                res = mid
            elif cur_dif == dif: # ! if equal sum(dif), the smaller number we guess(mid) should also update to res
                res = min(res, mid)
                
            if cur_sum - target == 0:
                return mid
            elif cur_sum - target > 0:
                r = mid - 1
            else:
                l = mid + 1
        
        return res
