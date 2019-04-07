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
    public int sumRootToLeaf(TreeNode root) {
        return sum(root, 0);
    }
    
    private int sum(TreeNode root, int tmp) {
        if (root == null) return 0;
        tmp = tmp * 2 + root.val;
        if(root.left == null && root.right == null) return tmp;
        return sum(root.left, tmp) + sum(root.right, tmp);
    }
}
