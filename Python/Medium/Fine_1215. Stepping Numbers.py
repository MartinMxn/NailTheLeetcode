"""
from 0 to 9, bfs generate number with in low to high range
"""
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        res = []
        
        def bfs(num, low, high, res):
            q = collections.deque([num])
            while q:
                nei = []
                for i in range(len(q)):
                    cur = q.popleft()
                    if cur >= low and cur <= high:
                        res.append(cur)
                    if cur == 0 or cur > high: # if cur == 0, will repeate generate
                        continue
                    last_digit = cur % 10
                    nei_p = last_digit + 1 + cur * 10
                    nei_m = last_digit - 1 + cur * 10
                    # if last digit is 0, just append plus one res
                    # if is 9, append minus one number
                    if last_digit == 0: 
                        nei.append(nei_p)
                    elif last_digit == 9:
                        nei.append(nei_m)
                    else:
                        nei.append(nei_p)  
                        nei.append(nei_m)
                q.extend(nei)
                
        for ele in range(10):
            bfs(ele, low, high, res)
            
        return sorted(res)
