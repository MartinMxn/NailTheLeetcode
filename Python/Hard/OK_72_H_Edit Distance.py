class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        '' to horse is 1 to 5
        so 
          '' h o r s e
        '' 0 1 2 3 4 5
        r  1 2 
        o  2
        s  3
        if same char, the cur step could come from without this single char(from dp[i - 1][j - 1])
        if not same, we have to insert/delete one char, so min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        replace | insert
        -----------------
        delete  | 
        """
        # space: O(min(n, m))
        n, m = len(word1), len(word2)
        pre = [i for i in range(m + 1)]

        for i in range(1, n + 1):
            cur = [0 for _ in range(m + 1)]
            cur[0] = i
            for j in range(1, m + 1):
                if word1[i - 1] != word2[j - 1]:
                    cur[j] = 1 + min(cur[j - 1], pre[j], pre[j - 1])
                else:
                    cur[j] = pre[j - 1]
            pre = cur
        
        return pre[-1]
                
