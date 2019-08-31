class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        t\s'' b a g b g b a g
        '' 1  1 1 1 1 1 1 1 1     # - empty is always a subseq of any str
        b  0  
        a  0              *
        g  0
        dp[i][j] -> the number of subseq of s[1:i] and t[1:j]
        
        **the purpose we build dp, we want to use the result we already calculated**
        
        if char is same, 
            so dp[i][j] = dp[i][j - 1]  jump this char
                            + dp[i - 1][j - 1] number of char we have except this char in s and t
        eg.AEDAE and AE
               ^      ^
               The E here result come from the previos result without this common E
        if not, the result will same as we dont have this char in t (seen as ignore to this char in s)
            so dp[i][j] = dp[i][j - 1]
        """
        ls, lt = len(s), len(t)
        prev = [1 for _ in range(ls + 1)]
        for i in range(1, lt + 1):
            cur = [0 for _ in range(ls + 1)]
            for j in range(1, ls + 1):
                if s[j - 1] == t[i - 1]:
                    cur[j] = cur[j - 1] + prev[j - 1]
                else:
                    cur[j] = cur[j - 1]
            prev = cur
            
        return prev[-1]
        
        
