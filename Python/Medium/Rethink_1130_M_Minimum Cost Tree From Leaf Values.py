class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        O(n^2)
        """
        res = 0
        for a in sorted(arr)[:-1]: # until the second last one so one of left and right is always valid
            i = arr.index(a)
            left = arr[i - 1] if i > 0 else float('inf')
            right = arr[i + 1] if i + 1 < len(arr) else float('inf')
            res += min(left, right) * a
            print(a, res)
            arr.pop(i)
        return res
            
