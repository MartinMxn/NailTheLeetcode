class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        '' to horse is 1 to 5
        so 
          '' h o r s e
        '' 0 1 2 3 4 5
        r  1
        o  2
        s  3
        if same char, the cur step could come from without this single char(from dp[i - 1][j - 1])
        if not same, we have to insert/delete one char, so min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        replace | insert
        -----------------
        delete  |  
        """
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)] 

        for i in range(n + 1):
            dp[i][0] = i
        
        for i in range(m + 1):
            dp[0][i] = i
            
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        
        return dp[-1][-1]
    
