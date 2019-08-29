# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def helper(start, end):
            res = []
            if start > end:
                return [None] # None is necessary since we need iterate the list every time
            for i in range(start, end + 1):
                left_sub = helper(start, i - 1) # i - 1 caz end + 1 above this line
                right_sub = helper(i + 1, end)
                for l in left_sub:
                    for r in right_sub:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        res.append(current_tree)
                        print(res)
                
            return res
        
        return helper(1, n)
            
