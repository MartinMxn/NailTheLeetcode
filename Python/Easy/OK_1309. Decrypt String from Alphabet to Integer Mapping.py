class Solution:
    """
    ASCII, a is 97, so 1 -> a, just + 96
    """
    def freqAlphabets(self, s: str) -> str:
        s = s[::-1]
        i = 0
        n = len(s)
        res = ""
        while i < n:
            if s[i] == '#':
                num = int(s[i + 2]) * 10 + int(s[i + 1])
                res += chr(num + 96)
                i += 3
            else:
                res += chr(int(s[i]) + 96)
                i += 1
                
        return res[::-1]
                
