import collections

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        if not points:
            return res
        
        def gcd(a, b): # greatest common divisor
            if b == 0:
                return a
            return gcd(b, a % b)
        
        n = len(points)
        for i in range(n):
            pairs = collections.defaultdict(int)
            duplicates = 1
            for j in range(i + 1, n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    duplicates += 1
                    continue
                de_x = points[j][0] - points[i][0]
                de_y = points[j][1] - points[i][1]
                print('x', de_x, 'y', de_y)
                d = gcd(de_x, de_y)
                print(d)
                pairs[(de_x//d, de_y//d)] += 1
            
            res = max(res, duplicates)
            for ele in pairs:
                res = max(pairs[ele] + duplicates, res)
        
        return res
                
