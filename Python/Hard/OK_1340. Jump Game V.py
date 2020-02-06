import functools

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        @functools.lru_cache(None)
        def max_dis(idx):
            mx = 0
            for dr in [1, -1]:
                for ds in range(1, d + 1): # start from 1, to d steps
                    nxt_x = idx + dr * ds
                    if 0 <= nxt_x < len(arr) and arr[nxt_x] < arr[idx]:
                        mx = max(mx, max_dis(nxt_x))
                    else:
                        break
            return mx + 1 # for any step, even not move, it counts as 1
        
        return max(max_dis(i) for i in range(len(arr)))
