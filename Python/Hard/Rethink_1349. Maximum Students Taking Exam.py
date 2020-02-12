from functools import lru_cache

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        if not len(seats) or not len(seats[0]):
            return 0
        
        rl, cl = len(seats), len(seats[0])
        def getNextSeat(x,y):
            return (x, y + 1) if y < cl - 1 else (x + 1, 0)
                    
        
        #transform the mask when switch to a new row by truncate the first "cl"
        #number of digit in the binary representation of the bit-mask number
        def transform(mask):
            ans = 0
            for i in range(cl, 2 * cl):
                if mask & 1 << i:
                    ans |= 1 << (i - cl)
            return ans
        
        #x and y is the row and column of current position, mask is a bit-mask number that records the seats being used
        #in the previous row and current row, so the length of binary representation of 'mask' is 2 * column number, where
		#first cl number of digit for previous row, and the rest for current row
        @lru_cache(None)
        def solve(x, y, mask):
            #reach the end
            if x == rl:
                return 0
            #reach a new row
            if not y:
                mask = transform(mask)
            #get the next seat x and y coordinates
            nextSeatX, nextSeatY = getNextSeat(x,y)
            #case that not to use current seat
            ans = solve(nextSeatX, nextSeatY, mask)
            if seats[x][y] == '#':
                return ans
            #Check the other seats nearby
            for d in ((0,-1),(-1,1),(-1,-1)):
                nx, ny = x + d[0], y + d[1]
                #Found a nearby seat being used, which makes current seat unavailable
                if 0 <= nx < rl and 0 <= ny < cl and mask & 1 << ((nx == x) * cl + ny):
                    break
            else:
                #Case that occupy the seat at current position
                ans = max(ans, solve(nextSeatX, nextSeatY, mask | 1 << (cl + y)) + 1)
            return ans
        
        return solve(0,0,0)
