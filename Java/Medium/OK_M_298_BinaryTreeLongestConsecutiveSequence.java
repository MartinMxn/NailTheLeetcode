/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class OK_M_298_BinaryTreeLongestConsecutiveSequence {
    int maxLen = 0;
    public int longestConsecutive(TreeNode root) {
        findLength(root, null, 0);
        return maxLen;
    }
    
    private void findLength(TreeNode root, TreeNode parent, int length) {
        if(root == null) return;
        length = (parent != null && root.val == parent.val + 1) ? length + 1 : 1;
        maxLen = Math.max(length, maxLen);
        findLength(root.left, root, length);
        findLength(root.right, root, length);
    }
}
