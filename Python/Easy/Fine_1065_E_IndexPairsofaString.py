class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        '''
        brute force find
        O(m * n)
        '''
        # pairs = []
        # for i in range(len(words)):
        #     start = text.find(words[i])
        #     while start != -1:
        #         pairs.append((start, start + len(words[i]) - 1))
        #         start = text.find(words[i], start + 1) # find start from the cur find position next charcter
        # pairs.sort()
        # return [[i,j] for i, j in pairs]
    
        '''
        trie tree
        '''
        trie = Trie(words).trie
        res = []
        start = -1
        for i, c in enumerate(text):
            if c in trie:
                start = i
                cur = trie[c]
                for j in range(i + 1, len(text)):
                    if "end" in cur:
                        res.append([start, j - 1])
                    if text[j] in cur:
                        cur = cur[text[j]]
                    else:
                        cur = None
                        break;
                if cur and "end" in cur:
                    res.append([start, len(text) - 1])
        return res
                    

class Trie:
    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            cur = self.trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["end"] = True
