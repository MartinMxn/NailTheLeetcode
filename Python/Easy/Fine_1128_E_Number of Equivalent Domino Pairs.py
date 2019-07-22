import collections

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        find pairs
        1 build a dict to store the previous pairs in dict
        2 the count is increase as arithmetic progression so add 1 after each time find same key
        """
        d = {}
        cnt = 0
        for i, j in dominoes:
            k, l = (i, j) if i <= j else (j, i)
            key = (k, l)
            if key not in d:
                d[key] = 0
                
            cnt += d[key]
            d[key] +=1
            
        
        return cnt
