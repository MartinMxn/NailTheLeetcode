class Solution:
    """
    XOR[l, r] = XOR[0, l - 1] ^ XOR[0, l - 1] ^ XOR[l, r]
              = XOR[0, l - 1] ^ XOR[0, r]
    """
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre, res = [0] * (len(arr) + 1), []
        
        for idx in range(len(arr)):
            pre[idx] = pre[idx - 1] ^ arr[idx]
        
        for x, y in queries:
            res.append(pre[y] ^ pre[x - 1])
        
        return res
