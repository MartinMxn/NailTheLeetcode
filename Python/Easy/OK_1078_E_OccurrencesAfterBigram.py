class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        arr = text.split(" ")
        for i in range(2, len(arr)):
            if (arr[i - 2] == first and arr[i - 1] == second):
                res.append(arr[i])
                
        return res
