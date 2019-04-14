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
    int maxAbs;
    public int maxAncestorDiff(TreeNode root) {
        findMaxAbs(root, Integer.MAX_VALUE, Integer.MIN_VALUE);
        return maxAbs;
    }
    
    private void findMaxAbs(TreeNode root, int min, int max) {
        if (root == null) return;
        max = Math.max(root.val, max);
        min = Math.min(root.val, min);
        maxAbs = Math.max(Math.abs(max - min), maxAbs);
        findMaxAbs(root.left, min, max);
        findMaxAbs(root.right, min, max);
    } 
}
