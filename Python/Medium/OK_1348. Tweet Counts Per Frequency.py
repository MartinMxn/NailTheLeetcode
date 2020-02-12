class TweetCounts:

    def __init__(self):
        self.mp = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.mp[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
#         if tweetName not in self.mp:
#             return []
        
#         interval = 0
#         if freq == 'minute':
#             interval = 60
#         elif freq == 'hour':
#             interval = 3600
#         else:
#             interval = 3600 * 24
        
#         ls = sorted(self.mp[tweetName])
        
        
#         idx = 0
#         res = []
        
#         # binary search to improve
#         while startTime <= endTime:
#             cur_count = 0
            
#             while idx < len(ls) and ls[idx] < startTime:
#                 idx += 1
#             while idx < len(ls) and ls[idx] < min(startTime + interval, endTime + 1):
#                 cur_count += 1
#                 idx += 1
#             startTime += interval
#             res.append(cur_count)
        
#         return res

        ls = self.mp[tweetName]
        left_idx = bisect.bisect_left(ls, startTime)
        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 3600
        elif freq == 'day':
            delta = 3600 * 24
            
        res = [0]*((endTime-startTime)//delta+1)
        # print (endTime, startTime, res)
        for time in ls[left_idx:]:
            if time > endTime:
                break
            res [(time-startTime)//delta] += 1
        return res
            

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
