class Solution:
    def printVertically(self, s: str) -> List[str]:
        if not s:
            return []
        ls = s.split()
        mx = 0
        for l in ls:
            mx = max(mx, len(l))

        res = []
        j = 0
        while j < mx:
            cur = ""
            for i in range(len(ls)):
                if j < len(ls[i]):
                    cur += ls[i][j]
                else:
                    cur += ' '
            res.append(cur.rstrip())
            j += 1
        return res
