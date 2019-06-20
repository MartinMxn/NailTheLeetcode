class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        d = collections.defaultdict(list)
        
        for idx, val in items:
            heapq.heappush(d[idx], val)
            if len(d[idx]) > 5:
                heapq.heappop(d[idx])
        
        res = collections.defaultdict(list)
        
        return [[i, sum(d[i]) // len(d[i])] for i in d]
        
