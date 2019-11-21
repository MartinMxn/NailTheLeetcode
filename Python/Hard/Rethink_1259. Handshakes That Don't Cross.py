class Solution:
    def numberOfWays(self, num_people: int) -> int:
        # even number of people
        dp = {0: 1, 2: 1}
        def divide(num):
            if num in dp:
                return dp[num]
            dp[num] = 0
            for i in range(0, num, 2):
                dp[num] = (dp[num] + divide(i) * divide(num - 2 - i)) % (10**9 + 7)
            
            return dp[num]
        
        return divide(num_people)
