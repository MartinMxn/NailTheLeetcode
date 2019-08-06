class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # """
        # from the first char, deconstruct to subproblem
        # (aab, azb)
        # 1 + (ab, zb)
        # 1 +     max(aa, a   |   a, az)
        # 1 + max(1 + (a, '') | max('', az | a, a) )
        # 1 + 1
        # 2
        # """
#         O(2^nm)
#         without memo
#         def lcs(i, j):
#             if i >= len(text1) or j >= len(text2):
#                 return 0
#             if text1[i] == text2[j]:
#                 return 1 + lcs(i + 1, j + 1)
#             else:
#                 return max(lcs(i, j + 1), lcs(i + 1, j))

#         return lcs(0, 0)

        # dp
        # O(nm)
        # O(nm)
        # """
        #   '' a b c d e
        # '' 0 0 0 0 0 0
        # a  0
        # c  0
        # e  0
        # """
#         n, m = len(text1), len(text2)
#         dp = [[0] * (m + 1) for i in range(n + 1)]
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = 1 + dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
#         return dp[-1][-1]
    
        # optimize space dp
        # O(nm)
        # O(n)
        # Take the shorter string first, set to text1
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        n, m = len(text1), len(text2)
        pre_dp = [0] * (n + 1)
        cur_dp = [0] * (n + 1)
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur_dp[i] = 1 + pre_dp[i - 1]
                else:
                    cur_dp[i] = max(cur_dp[i - 1], pre_dp[i])
            pre_dp, cur_dp = cur_dp, pre_dp # assign it to previous one
            
        return pre_dp[-1]
        
