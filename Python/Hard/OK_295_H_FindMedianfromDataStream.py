class MedianFinder:
    # two heap
    def __init__(self):
        """
        initialize your data structure here.
        max heap for smaller part
        min heap for larger part
        !: if len are equal, push to max
        but push to min and pop tmp, them push tmp to max
        vice versa
        """
        self.max_heap = []
        self.min_heap = []
    def addNum(self, num: int) -> None:
        if (len(self.max_heap) == len(self.min_heap)):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))

    def findMedian(self) -> float:
        if (len(self.max_heap) == len(self.min_heap)):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
