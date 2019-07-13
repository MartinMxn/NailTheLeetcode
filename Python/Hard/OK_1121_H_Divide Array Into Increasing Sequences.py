class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        count = collections.Counter(nums)
        print(count.values())
        groups = max(count.values())
        return len(nums) >= K * groups
