class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # brute force
        # need imporve
        n = len(text)
        s = set()
        
        for i in range(n + 1):
            for j in range(i):
                if (i - j) % 2 != 0:
                    continue
                if text[j:(i + j) // 2] == text[(i + j) // 2:i]:
                    s.add(text[j: i])
                    
        return len(s)
