class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """
        arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
        arr1: 4-1=3 
        arr2: 6-(-1)=7
        index: 3-0=3
            |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
        =   max(arr1[i] - arr1[j], arr1[j] - arr1[i]) + max(arr2[i] - arr2[j], arr2[j] - arr2[i])
        so we need to compare these 4 formula
        set the init closest distance int value at index 0
        compare with it when iterating the array
        update res and closest at same time
        """
        res = 0
        
        for off_1, off_2 in [[-1, 1], [-1, -1], [1, 1], [1, -1]]:
            closest = arr1[0] * off_1 + arr2[0] * off_2
            for i in range(len(arr1)):
                cur = arr1[i] * off_1 + arr2[i] * off_2 + i
                res = max(res, cur - closest)
                closest = min(cur, closest)
        
        return res
