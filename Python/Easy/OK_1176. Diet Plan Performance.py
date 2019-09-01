class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        cur_sum, res = 0, 0
        n = len(calories)
        for i in range(k):
            cur_sum += calories[i]
        if cur_sum < lower:
            res -= 1
        elif cur_sum > upper:
            res += 1
        
        for i in range(k, n):
            cur_sum += calories[i]
            cur_sum -= calories[i - k]
            if cur_sum < lower:
                res -= 1
            elif cur_sum > upper:
                res += 1
        
        return res
