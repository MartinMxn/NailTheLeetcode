"""
s = "aab"
p = "c*a*b"
     0 c * a * b
   0 1 0 1 0 1 0
   a 0
   a 0
   b 0
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        # if pattern is a*, it could match with empty string
        for i in range(1, m + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] # ignore the (char)* in pattern and get the previous result
                    # check the char before * is same or not
                    # if same, then check result that the s without that char with cur pattern((char)* pattern)
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.': 
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = False
                    
        return dp[-1][-1]
                
