class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            res = sum((i // m + 1 if i % m else i // m) for i in nums)
            if res > threshold:
                l = m + 1
            else:
                r = m
        return l
