class Solution:
    # 2^N if without cache
    # "@functools.lru_cache(None)" caches all the input and out put of "dp"   
    # so that when the same input comes again, it will immediately return the cached result calculated last time.
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        cnt = collections.Counter(letters)
        
        @functools.lru_cache(None)
        def dp(word_idx, cnt):
            if word_idx >= len(words):
                return 0
            tmp_c = copy.copy(cnt)
            res = 0
            for c in words[word_idx]:
                if tmp_c[c] > 0:
                    tmp_c[c] -= 1
                    res += score[ord(c) - ord('a')]
                else:
                    res = 0
                    break
                    
            res += dp(word_idx + 1, tmp_c)
            return max(res, dp(word_idx + 1, cnt))
            
        return dp(0, cnt)
