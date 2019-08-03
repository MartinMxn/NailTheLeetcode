class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        t % 60 will range 0 - 59, but
        (60 - t % 60) % 60 will get number in range 1 ~ 60.
        [30,20,150,100,40]
        mp: {
            30:1
            20:1
            150:1
            100:1
            40:1
        }
        
        [60,60,60]
        mp: {
            60:1->2->3
        }
        """
        mp = collections.defaultdict(int)
        res = 0
        for t in time:
            res += mp[(60 - t % 60) % 60] # 0 -> 0, 1 -> 1, 60 -> 60
            mp[t % 60] += 1
        
        return res
                
