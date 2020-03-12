class Solution:
    # O(m + n)/O(m + n)
    #     def backspaceCompare(self, S: str, T: str) -> bool:
    #         def itr(string, stack):
    #             for s in string:
    #                 if s == '#':
    #                     if stack:
    #                         stack.pop()
    #                 else:
    #                     stack.append(s)
    #             return stack

    #         return itr(S, []) == itr(T, [])

    # O(n)/O(1)
    def backspaceCompare(self, S1, S2):
        r1 = len(S1) - 1
        r2 = len(S2) - 1

        def getChar(s, r):
            char, count = '', 0
            while r >= 0 and not char:
                if s[r] == '#':
                    count += 1
                elif count == 0:
                    char = s[r]
                else:
                    count -= 1
                r -= 1
            return char, r

        while r1 >= 0 or r2 >= 0:  # or here, not 'and'
            char1, char2 = '', ''
            if r1 >= 0:
                char1, r1 = getChar(S1, r1)
            if r2 >= 0:
                char2, r2 = getChar(S2, r2)
            if char1 != char2:
                return False
        return True


s = Solution()
s.backspaceCompare("bbb", "bbb#")
