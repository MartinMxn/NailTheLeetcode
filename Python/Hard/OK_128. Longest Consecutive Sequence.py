class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n)
        if not nums:
            return 0
        
        res = 0
        num_set = set(nums)
        for num in nums:
            # avoid the repeat calculate, if consecutive, the num - 1 must in set
            # this makes the seq we count always start from the first one
            if num - 1 not in num_set: 
                # if not, the seq may start from this num
                cur_num = num
                cur_len = 1
                
                while cur_num + 1 in num_set:
                    cur_len += 1
                    cur_num += 1
                
                res = max(res, cur_len)
                
        return res
                
