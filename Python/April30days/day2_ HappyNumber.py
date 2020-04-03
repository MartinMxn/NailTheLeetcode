class Solution:
    def isHappy(self, n: int) -> bool:
        # O(logn) O(logn)
#         visited = set()
        
#         while n != 1:
#             s = 0
#             while n > 0:
#                 s += (n % 10) ** 2
#                 n //= 10
            
#             if s not in visited:
#                 visited.add(s)
#             else:
#                 return False
#             n = s
            
#         return True
        
        # O(logn) O(1)
        # fast/slow pointer
        
        def get_next(n):
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            return s
        
        slow, fast = n, get_next(n)
        print(slow, fast)
        while slow != fast and fast != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast == 1
