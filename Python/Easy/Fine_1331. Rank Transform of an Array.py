class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        r = {}
        for a in sorted(arr):
            r.setdefault(a, len(r) + 1)
        return map(lambda x: r[x], arr)
        
