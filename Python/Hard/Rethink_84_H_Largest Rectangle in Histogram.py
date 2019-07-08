class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        # brute force TLE
#         if len(nums) == 0:
#             return 0
#         res = nums[0]
#         pt = 0
        
#         def check(nums, end_idx):
#             res = min_v = nums[pt]
#             for i in range(end_idx, -1, -1):
#                 min_v = min(nums[i], min_v)
#                 res = max(res, min_v * (end_idx - i + 1))
#             return res
            
#         while pt < len(nums) - 1:
#             if nums[pt + 1] < nums[pt]:
#                 max_v = check(nums, pt)
#                 res = max(max_v, res)
#             elif nums[pt + 1] == nums[pt]:
#                 max_v = check(nums, pt + 1)
#                 res = max(max_v, res)
#             pt += 1
#         res = max(res, check(nums, pt)) # check at then end, prevent all increasing case
#         return res
    
        # stack
