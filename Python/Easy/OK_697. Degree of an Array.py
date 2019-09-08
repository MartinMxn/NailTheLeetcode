class Solution:
    """
    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation: 
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.
    
    update the first appearance pos and count while traversing the list
    if not appeared before, setdefault first appear pos
    if count > max+degree, update max_degree and update res
    but if count == max_degree, just update res
    
    # deal with > and == seperately
    """
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_appear = {}
        res, max_degree = 0, 0
        count = collections.Counter(nums)
        
        for i, v in enumerate(nums):
            first_appear.setdefault(v, i)
            count[v] = count.get(v, 0) + 1
            if count[v] > max_degree:
                max_degree = count[v]
                res = i - first_appear[v] + 1
            elif count[v] == max_degree:
                res = min(res, i - first_appear[v] + 1)
                
        return res
        
        
