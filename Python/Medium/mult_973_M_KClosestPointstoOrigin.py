class Solution:
    '''
    sort O(nlon)
    '''
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     points.sort(key = lambda pair: pair[0] ** 2 + pair[1] ** 2)
    #     return points[:K]
    '''
    heap O(nlogk)
    '''
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        hp = []
        
        for (x, y) in points:
            dist = x*x + y*y
            heapq.heappush(hp, (-dist, [x, y]))
            if len(hp) > K:
                heapq.heappop(hp)
            
        return [heapq.heappop(hp)[1] for _ in range(K)]
    '''
    quick sort
    avg: O(n) wrost:O(n^2)
    ...
    '''
