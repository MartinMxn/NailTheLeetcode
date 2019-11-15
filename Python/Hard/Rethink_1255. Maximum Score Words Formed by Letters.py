class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def check_valid(mask, word):
            word = collections.Counter(word)
            
            nxtMask = mask
            for i in range(len(letters)):
                if not ((mask >> i) & 1) and letters[i] in word:
                    word[letters[i]] -= 1
                    if word[letters[i]] == 0:
                        word.pop(letters[i])
                    nxtMask ^= (1 << i)
                else:
                    continue
            
            if word:
                return (False, 0)
            return (True, nxtMask)
        
        global dp
        dp = {}
        
        def search(curMask, start):
            if curMask in dp:
                return dp[curMask]
            
            cur_score = 0
            
            for i in range(start, len(words)):
                is_valid, nxt_mask = check_valid(curMask, words[i])
                if is_valid:
                    word_score = 0
                    for c in words[i]:
                        word_score += score[ord(c) - ord('a')]
                    cur_score = max(word_score + search(nxt_mask, i + 1), cur_score)
                
            dp[curMask] = cur_score
            return cur_score
        
        return search(0, 0)
