import functools

class Solution:
    """ 
    abcdefg
    i     j
    dp[i][j] = minimum step to make s[i ~ j] palindrome
    if s[i] == s[j] -> i + 1 ~ j - 1 subproblem
    if  ..  != ..   -> add s[i] after s[j] -> dp[i + 1 ~ j] + 1 
                    -> or add s[j] before s[i] -> dp[i ~ j - 1] + 1
    """
    
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dp(i + 1, j - 1)
            else:
                return min(dp(i + 1, j), dp(i, j - 1)) + 1 # don't care the str after insertion
        
        return dp(0, len(s) - 1)
