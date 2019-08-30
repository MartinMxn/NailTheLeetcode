class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
           '' b a g b g b a g
        '' 1  1 1 1 1 1 1 1 1     # - empty is always a subseq of any str
        b  0  1 1 1 2 2 3 3 3
        a  0  1 2
        g  0
        dp[i][j] -> the res at s[i], s[j]
        if char is same, 
            so dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] ???
        if not, the result will same as we dont have this char in t
            so dp[i][j] = dp[i][j - 1]
        """
