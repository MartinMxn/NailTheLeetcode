class Solution:
    """
    0 1 3 5 6
    for stone 6, may from 1,1,1,... or 1,2,3
    so we need to store all possible previous step to 6
    so we need a dict for each position
    
    each time we reach a new pos
    update the possible set at this pos with -1, 1 for each number in set
    Lastly check wether the last step is not an empty set
    """
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        # create dict with set for each position
        steps = {}
        for x in stones:
            steps[x] = set()
        
        # position 1(first step) must be 1 
        steps[1].add(1)
        
        for i in range(1, len(stones)):
            for j in steps[stones[i]]:
                for nj in [j - 1, j, j + 1]:
                    if nj > 0 and stones[i] + nj in steps: # > 0 is necessary
                        steps[stones[i] + nj].add(nj)
        
        return steps[stones[-1]] != set()
    
