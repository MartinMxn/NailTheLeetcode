"""
Input:
[
  "wrt",
  "wrf", t->f
  "er",  w->e
  "ett", r->t
  "rftt" e->r
]

Output: "wertf"
"""

# Assumption:
# 1. all lower letter case ?
# 2. order is valid? Yes, No -> return ""
# 3. maybe multiple order, return any, if lexicographically -> ok

from collections import deque, defaultdict

class Solution:
    def alienOrder(self, words) -> str:
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        res = ''

        for word in words:
            for c in word:
                in_degree[c] = 0

        for pair in zip(words[:-1], words[1:]):
            # pair -> (wrt, wrf), (wrf, er)...
            for c1, c2 in zip(*pair):
                # c1 c2 -> w,w r,r t,f...
                # ! special case here if you meet a->b twice
                # should just add one in_degree['b']
                # so use a tmp set to handle this
                # print('before build', c1, c2, graph)
                if c1 != c2:
                    char_set = set()
                    if c1 in graph:
                        char_set = graph[c1]
                    if c2 not in char_set:
                        char_set.add(c2)
                        # print('build', c1, c2)
                        graph[c1] = char_set
                        in_degree[c2] += 1
                        break

        q = deque([c for c in in_degree if in_degree[c] == 0])

        while q:
            nxt_q = deque()
            q = deque(sorted(list(q))) # follow up, sort it each time
            size = len(q)
            for _ in range(size):
                c = q.popleft()
                res += c
                for nxt in graph[c]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        nxt_q.append(nxt)
            q = nxt_q

        if len(res) == len(in_degree.keys()):
            return res

        return ""
    
