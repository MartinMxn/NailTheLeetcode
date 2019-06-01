class Solution:
    '''
    Use dict to store the word
    check whether the word that remove one letter exist in dict
    if so, add one and update the current word in dict
    compare with the max variable and update the longest result
    O(n * l) l = longest length of word
    O(n)
    n = len(words)
    '''
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        word_dict = {}
        
        for word in words:
            word_dict[word] = 1
        
        maxLen = 1
        for word in words:
            for i in range(len(word)):
                remove_i_letter = word[:i] + word[i + 1:]
                if (remove_i_letter in word_dict):
                    word_dict[word] = word_dict[remove_i_letter] + 1
                    maxLen = max(maxLen, word_dict[word])
                    break
        
        return maxLen
