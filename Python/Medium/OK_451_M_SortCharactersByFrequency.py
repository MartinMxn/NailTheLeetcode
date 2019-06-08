class Solution:
    '''
    bucket sort
    '''
    def frequencySort(self, s: str) -> str:
        if not s:
            return ''
        c1, c2 = collections.Counter(s), {}
        for k,v in c1.items():
            c2.setdefault(v, []).append(k*v)
        # {1: ['t', 'r'], 2: ['ee']}
        # output reverse from the most freq one
        return ''.join([''.join(c2[i]) for i in range(len(s), -1, -1) if i in c2])

        
