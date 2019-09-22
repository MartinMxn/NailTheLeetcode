"""
count bulls and record other number
traverse twice and find cows
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = collections.defaultdict(int)
        A, B = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                count[secret[i]] += 1
        
        for i in range(len(secret)):
            if secret[i] != guess[i] and count[guess[i]] > 0:
                B += 1
                count[guess[i]] -= 1
        
        return str(A) + 'A' + str(B) + 'B'
