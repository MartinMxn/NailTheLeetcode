class Solution:
    """
    if only has positive number, just two pointer
    find the cur_sum larger than num and move the left pointer
    
    but may has negative number
      [2,-1,2]
    [0,2, 1,3]
    """
    # O(n^2)
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
    """
    Based on prefix sum
    2 -1 2 4 -5 6 10
  0 2  1 3 7  2 8 12
  
  the sum of 4 to 6 is 8 - 3 = 5, which is pre_sum[i] - pre_sum[j - 1]
  we need to find the minimum length of sum > K
  if the pre_sum value is increase, which means the pre sum is increase, the shorter interval must appear before 
  so we pop out this current last pre_sum index
  and once the pre_sum j to i is larger than K, we should compare with the res and popleft since we already use that
  and the later index must longer than the current i
    """
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        pre_sum = [0]
        dq = collections.deque([0])
        res = float('inf')
        for a in A:
            pre_sum.append(pre_sum[-1] + a)
        
        for i in range(n + 1):
            while dq and pre_sum[i] <= pre_sum[dq[-1]]:
                dq.pop()
            while dq and pre_sum[i] - pre_sum[dq[0]] >= K:
                res = min(res, i - dq.popleft())
            dq.append(i)
            
        return res if res != float('inf') else -1
