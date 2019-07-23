# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    1. 
    find the medium node each time
    smaller part be the left node and larger part is right node
    O(nlogn)
    O(logn)

    2.
    trade off space for time
    convert to list and build the bst
    O(n)
    O(n)
    """
    # 1
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         if not head:
#             return None
#         if not head.next:
#             return TreeNode(head.val)
        
#         def find_mid(root):
#             slow = fast = root
#             prev = None
#             while fast and fast.next:
#                 prev = slow
#                 slow = slow.next
#                 fast = fast.next.next
            
#             prev.next = None # ! need to cut
#             return slow
        
#         # cur the cur list by find_mid
#         mid = find_mid(head)
#         root = TreeNode(mid.val)
#         root.left = self.sortedListToBST(head)
#         root.right = self.sortedListToBST(mid.next)
#         return root
    
    # 2
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def convert_to_list(head):
            res = []
            while head:
                res.append(head.val)
                head = head.next
            return res
                
        ls = convert_to_list(head)
        
        def build_tree(l, r):
            if l > r:
                return None
            
            mid = l + (r - l) // 2
            root = TreeNode(ls[mid])
            if l == r:
                return root
            
            root.left = build_tree(l, mid - 1)
            root.right = build_tree(mid + 1, r)
            
            return root
        
        return build_tree(0, len(ls) - 1)
