class Solution:
    """
    if only has positive number, just two pointer
    find the cur_sum larger than num and move the left pointer
    
    but may has negative number
      [2,-1,2]
    [0,2, 1,3]
    """
    # O(n^@)
#     def shortestSubarray(self, A: List[int], K: int) -> int:
#         prefix = [0]
#         for a in A:
#             prefix.append(prefix[-1] + a)
#         # prefix[i] - prefix[j - 1] is the sum of j to i
#         res_len = float('inf')
#         for i in range(1, len(A) + 1):
#             for j in range(i):
#                 diff_prefix = prefix[i] - prefix[j]
#                 if diff_prefix >= K:
#                     res_len = min(res_len, i - j)
        
#         return res_len if res_len != float('inf') else -1
    
    # O(n)
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        pre_sum = [0]
        for a in A:
            pre_sum.append(pre_sum[-1] + a)
        res = float('inf')
        dq = collections.deque([0])
        for i in range(n + 1):
            while dq and pre_sum[i] - pre_sum[dq[0]] >= K:
                res = min(res, i - dq.popleft())
            while dq and pre_sum[i] <= pre_sum[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        return res if res != float('inf') else -1
