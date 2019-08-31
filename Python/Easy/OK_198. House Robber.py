class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [A,B,C,D,E]
        A -> CDE
        NOT A -> BCDE
        """
        # O(n)
#         n = len(nums)
#         dp_r = [0 for _ in range(n + 1)]
#         dp_nr = [0 for _ in range(n + 1)]
#         for i in range(1, n + 1):
#             dp_r[i] = dp_nr[i - 1] + nums[i - 1]
#             dp_nr[i] = max(dp_r[i - 1], dp_nr[i - 1])
        
#         return max(dp_nr[-1], dp_r[-1])
    
        # O(1) space
        pre_r, pre_nr = 0, 0
        n = len(nums)
        for i in range(1, n + 1):
            tmp_r = pre_r
            pre_r = pre_nr + nums[i - 1]
            pre_nr = max(pre_nr, tmp_r)
            
        return max(pre_r, pre_nr)
