class Solution:
    def expand(self, S: str) -> List[str]:
        A = S.replace('{', ' ').replace('}', ' ').strip().split(' ') # a,b c d,e f
        B = [a.split(',') for a in A] # [a,b], c, [d,e], f
        # res = [[]]
        # for item in B:
        #     res = [x + [y] for x in res for y in item] # [[a,c,d,f],[a,c,e,f]...]
        # ans = []
        # for item in res:
        #     ans.append("".join(item))
        return sorted("".join(c) for c in itertools.product(*B))
