class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        l = [(s.lower(), s.upper()) if s.isalpha() else s for s in S]
        return ["".join(i) for i in itertools.product(*l)]
