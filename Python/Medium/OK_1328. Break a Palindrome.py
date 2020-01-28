class Solution:
    """
    p is already a panlidrome
    !!! break by lexicographically smallest 
    """
    def breakPalindrome(self, p: str) -> str:
        n = len(p)
        if n <= 1:
            return ""
        
        for i in range(n // 2):
            if p[i] != 'a':
                return p[:i] + 'a' + p[i + 1:]

        return p[:-1] + 'b'
