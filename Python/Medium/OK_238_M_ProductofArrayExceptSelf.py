class Solution:
    '''
    store the previous product from 1 to last at first loop
    get the result by multiple the res from last 
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            arr[i] = arr[i - 1] * nums[i - 1]
        
        res = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            arr[i] *= res
            res *= nums[i]
        return arr
