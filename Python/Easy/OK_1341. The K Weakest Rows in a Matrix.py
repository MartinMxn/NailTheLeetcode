class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        w = [(sum(mat[i]), i) for i in range(len(mat))]
        # the tuple in python sort by 1st, then 2nd, so the 2nd'd be useful for sequence
        return [i for v, i in sorted(w)[:k]]
