class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        str1 = "abac"
        str2 = "cab"
        find lcs  = "ab"
        then combine
        """
        def find_lcs(s1, n, s2, m):
            if m == 0 or n == 0: return ""
            dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
            return dp[-1][-1]
        
        n, m = len(str1), len(str2)
        lcs = find_lcs(str1, n, str2, m)

        res = ""
        i, j = 0, 0
        for c in lcs:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]
        
