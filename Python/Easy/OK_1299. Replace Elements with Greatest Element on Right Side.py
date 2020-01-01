class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        largest_from_right = [-1]
        cur_max = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            cur_max = max(cur_max, arr[i + 1])
            largest_from_right.insert(0, cur_max)
        
        return largest_from_right
