class Solution:
    """
    brute force: try all pairs and verify whether is a palindrome
    n^2*len len is the max length of word
    
    for palin pairs, it could be bat+ab or ba+ab
    we could get substr if 2nd part is palin then the reversed 1st part also exist
    dict to store all the word's position
    for each word, calculate every substring pairs could be divided 
    and see whether the reversed itself exist in the dict
    O(n * len^2)
    """
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            l = len(s)
            for i in range(l // 2):
                if s[i] != s[l - i - 1]:
                    return False
            return True
        
        mp = {word: i for i, word in enumerate(words)}
        
        res = set() # distinct indices
        for i, word in enumerate(words):
            for j in range(len(word) + 1): # + 1 -> [:j] in python end 1 before j
                p1 = word[:j]
                p2 = word[j:]
                if is_palindrome(p1) and p2[::-1] in mp and mp[p2[::-1]] != i:
                    res.add((mp[p2[::-1]], i))
                if is_palindrome(p2) and p1[::-1] in mp and mp[p1[::-1]] != i:
                    res.add((i, mp[p1[::-1]]))
        
        return list(res)
            
        
