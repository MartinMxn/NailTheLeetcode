class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a2_set = set(arr2)
        a1_count = collections.Counter(arr1)
        res = []
        for i in range(len(arr2)):
            for j in range(a1_count[arr2[i]]):
                res.append(arr2[i])

        left = []
        for i in arr1:
            if i not in a2_set:
                left.append(i)
        for j in sorted(left):
            res.append(j)
        return res
