class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # TLE        
        # res = [0 for _ in range(n)]
        # for i in range(len(bookings)):
        #     b = bookings[i]
        #     for j in range(b[0] - 1, b[1]):
        #         res[j] += b[2]
        # return res
        
        # record changes and add at the end together
        change = [0] * (n + 2)
        for s, e, se in bookings:
            change[s] += se
            change[e + 1] -= se
        
        flight = 1
        tmp = 0
        res = []
        
        while flight <= n:
            tmp += change[flight]
            res.append(tmp)
            flight += 1
        
        return res
        
