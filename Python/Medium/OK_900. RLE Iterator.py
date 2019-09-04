# brute force, recover the whole array

# from collections import deque
# class RLEIterator:

#     def __init__(self, A: List[int]):
#         self.q = deque()
#         n = len(A)
#         for i in range(0, n, 2):
#             for _ in range(A[i]):
#                 self.q.append(A[i + 1])
        
#     def next(self, n: int) -> int:
#         last = -1
#         while n > 0 and self.q:
#             last = self.q.popleft()
#             n -= 1
#         if n > 0:
#             return -1
#         else:
#             return last

class RLEIterator:
    """
    [3,8,0,9,2,5]
    [2],[1],[1],[2]
    i = 0
    """
    def __init__(self, A: List[int]):
        self.A = A
        self.index = 0

    def next(self, n: int) -> int:
        if self.index >= len(self.A):
            return -1
        if self.A[self.index] < n:
            left = n - self.A[self.index]
            self.index += 2
            return self.next(left)
        else:
            self.A[self.index] -= n
            return self.A[self.index + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)900. RLE Iterator
