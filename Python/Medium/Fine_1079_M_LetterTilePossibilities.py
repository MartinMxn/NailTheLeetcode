class Solution:
    '''
    permutation
    '''
    def numTilePossibilities(self, tiles: str) -> int:    
        s = set()
        
        def helper(tiles, cur):
            if (cur in s):
                return
            if cur not in s or not tiles:
                s.add(cur)
            for i in range(len(tiles)):
                helper(tiles[:i] + tiles[i+1:], cur + tiles[i])
            
        helper(tiles, "") 
        return len(s) - 1   # remove ""
    
