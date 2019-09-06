# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    each list will be the vertical line | list
    level order traverse and store the number in list 
    then combine the list
    """
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = collections.defaultdict(list)
        q = [(root, 0)]
        while q:
            new_q = []
            tmp_list = collections.defaultdict(list)
            for node, pos in q:
                tmp_list[pos].append(node.val)
                if node.left:
                    new_q.append((node.left, pos - 1))
                if node.right:
                    new_q.append((node.right, pos + 1))
            for i in tmp_list:
                dic[i].extend(sorted(tmp_list[i])) # not append, extend is to add list to list
                # each item in the list will be append to list
            q = new_q
        
        return [dic[i] for i in sorted(dic)]
