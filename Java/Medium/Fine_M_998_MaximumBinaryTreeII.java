/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 
!!!! B[B.length-1] = val
!!! If val is the largest, i = B.length-1, the root node's value is val, i=0 to i-1 are in the left child of root.
This explains why when val > root.val, root should be the left child of new node with value val.

Else if val is not the largest, the new node with value val is always the right child of root.

 val append the end of array, so always right
 1. find the position where cur.right.val < val < cur.val
 2. insert the node to that, cur.right become the node.left, cur.right become the node
 */
class Solution {
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        TreeNode node = new TreeNode(val);
        TreeNode cur = root;
        if(root.val < val) {
            node.left = root;
            return node;
        }
        
        while(cur.right != null && cur.right.val > val) {
            cur = cur.right;
        }
        node.left = cur.right;
        cur.right = node;
        return root;
    }
}
