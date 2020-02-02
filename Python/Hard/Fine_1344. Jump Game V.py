import functools

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        @functools.lru_cache(None)
        def max_for_each_step(index):
            res = 0
            for dir in [-1, 1]:
                for x in range(1, d + 1):
                    nxt = index + x * dir
                    if 0 <= nxt < len(arr) and arr[nxt] < arr[index]:
                        res = max(res, max_for_each_step(nxt))
                    else:
                        break
                        
            return res + 1
        
        return max(max_for_each_step(i) for i in range(len(arr)) )
