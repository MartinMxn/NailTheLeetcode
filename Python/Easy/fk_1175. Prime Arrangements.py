from math import factorial

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = [True for _ in range(n + 1)]
        num = 2
        while num * num <= n:
            if prime[num]:
                for i in range(num * num, n + 1, num):
                    prime[i] = False
            num += 1
        prime_count = sum(prime[2:])
        return factorial(prime_count) * factorial(n - prime_count) % (10**9 + 7)
        
