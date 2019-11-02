class Solution:
    """
    dp, dp[i][j] -> number of steps to remove arr[i:j]
    if arr[j] == arr[i]:
        dp[i][j] = dp[i][j - 1]
    """
    def minimumMoves(self, arr: List[int]) -> int:
        if not arr:
            return 0
        n = len(arr)
        dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
        for l in range(1, n + 1):
            # loop with two variables i and j, denoting 
            # starting and ending of substrings 
            i, j = 0, l - 1
            
            while j < n:
                if l == 1:
                    dp[i][j] = 1
                else:
                    # the minimum situation is remove current num by 1 step
                    dp[i][j] = dp[i + 1][j] + 1
                    # if current and next num are same, choose min from current  
                    # and subproblem (i+2,j) 
                    if arr[i] == arr[i + 1]:
                        dp[i][j] = min(dp[i][j], dp[i + 2][j] + 1)
                        
                    ''' 
                    loop over all right num and suppose 
                    Kth num is same as ith character then 
                    choose minimum from current and two 
                    substring after ignoring ith and Kth num 
                    '''
                    for k in range(i + 2, j + 1):
                        if arr[i] == arr[k]: # ignore index k num of [i:j]
                            dp[i][j] = min(dp[i + 1][k - 1] + dp[k + 1][j], dp[i][j]) 
                    
                i += 1
                j += 1
        
        return dp[0][n - 1] # ?
