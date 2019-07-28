from collections import deque, defaultdict
"""
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
            t - f
          - w - e
        w - e - r
            r - t
            
]
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ''
        
        out = defaultdict(set)
        degree = {}
        res = ''
        
        for word in words:
            for c in word:
                degree[c] = 0
                
        for pair in zip(words, words[1:]):
            for c1, c2 in zip(*pair):
                if c1 != c2:
                    char_set = set()
                    if c1 in out:
                        char_set = out[c1]
                    if c2 not in char_set:
                        char_set.add(c2)
                        out[c1] = char_set
                        degree[c2] += 1
                    break
        """
        seen 
        {
            't': {'f'},
            'w': {'e'},
            'r': {'t'},
            'e': {'r'}
        }
        """
        
        # init the topo deque
        dq = deque()
        for c in degree.keys():
            if degree[c] == 0:
                dq.append(c)
        
        while dq:
            c = dq.pop()
            res += c
            if c in out:
                for c2 in out[c]:
                    degree[c2] -= 1
                    if degree[c2] == 0:
                        dq.append(c2)
        
        if len(res) != len(degree.keys()):
            return ""
        
        return res
                    
