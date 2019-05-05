/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int preValue = 0;
    public TreeNode bstToGst(TreeNode root) {
        //update node value with right subtree sum
        
        //right
        if (root.right != null) bstToGst(root.right);
        root.val += preValue;
        preValue = root.val;
        //left
        if (root.left != null) bstToGst(root.left);
        return root;
    }
}
