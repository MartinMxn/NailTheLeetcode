# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def encode(node):
            if not node:
                return "x"
            tmp = str(node.val)
            left = encode(node.left)
            right = encode(node.right)
            return tmp + "," + left + "," + right
        
        self.s = encode(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode(s_arr):
            if s_arr[0] == 'x':
                s_arr.popleft()
                return None
            cur = TreeNode(s_arr.popleft())
            cur.left = decode(s_arr)
            cur.right = decode(s_arr)
            return cur
            
        s_arr = self.s.split(",")
        return decode(collections.deque(s_arr)) # faster than dont convert to deque

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
