class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        '''
        Condition: sorted asc / distinct / return the smallest index
        1. loop over array and find smalleset
        2. binary search
        '''
        # 1 O(n)
#         for i in range(len(A)):
#             if (A[i] == i): return i
        
#         return -1
        
        #2 O(logn)
        low, high = 0, len(A) - 1
        while(low < high):
            mid = low + (high - low) // 2
            if A[mid] >= mid:
                high = mid
            else:
                low = mid + 1
        return low if low == A[low] else -1
