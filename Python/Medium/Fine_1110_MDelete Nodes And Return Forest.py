class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        self.labels = set()
        self.preorder(root, set(to_delete))
        return self.ans
    
    def preorder(self, node, to_delete, label=None):
        if node is None:
            return None
        if label is None:
            label = node.val
        
        if node.val not in to_delete:
            if label not in self.labels:
                self.labels.add(label)
                self.ans.append(node)
            node.left = self.preorder(node.left, to_delete, label)
            node.right = self.preorder(node.right, to_delete, label)
            return node
        else:
            self.preorder(node.left, to_delete)
            self.preorder(node.right, to_delete)
            return None
