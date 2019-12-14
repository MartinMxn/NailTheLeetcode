class Solution:
    """
    [3,3,3,3,3,1,3]
     0 1 2 3 4 5 6
    
    3: [0,1,2,3,4,6]
    1: [5]
    append [0,1,2] to res, then next three item
    # guaranteed that there exists at least one solution. 
    """
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            mp[size].append(i)
        
        res = []
        for s in mp:
            for i in range(0, len(mp[s]), s):
                res.append(mp[s][i: i + s])
        
        return res
