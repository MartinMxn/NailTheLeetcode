class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        c = collections.Counter(arr)
        cur_sum, times = 0, 0
        for v, i in sorted([(f, n) for n, f in c.items()], reverse=True): # sort by frequency first
            cur_sum += v
            times += 1
            if cur_sum >= n // 2:
                break
        
        return times
            
