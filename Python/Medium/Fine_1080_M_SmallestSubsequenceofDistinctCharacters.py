class Solution:
    '''
    Monotonic stack
    
    Input: "cdadabcc"
    Output: "adbc"
    '''
    def smallestSubsequence(self, text: str) -> str:
        freq = {c: i for i, c in enumerate(text)}
        # last index of each character
        # {'c': 7, 'd': 3, 'a': 4, 'b': 5}
        print(freq)
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and c < stack[-1] and freq[stack[-1]] > i: # could appear later
                stack.pop()
            stack.append(c)
        
        return ''.join(stack)
