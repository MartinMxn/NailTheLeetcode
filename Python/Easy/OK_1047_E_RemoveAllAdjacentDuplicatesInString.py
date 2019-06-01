class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in range(len(S)):
            if stack and S[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(S[i])
        return "".join(stack)
