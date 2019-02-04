/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class OK_E_572_SubtreeofAnotherTree {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(s == null) return false;
        if(varify(s, t)){
            return true;
        }else {
            return isSubtree(s.left, t) || isSubtree(s.right, t);
        }
    }
    
    private boolean varify(TreeNode s, TreeNode t) {
        if(s == null && t == null) return true;
        if(s == null || t == null) return false;
        if(s.val != t.val) return false;
        boolean checkLeft = varify(s.left, t.left);
        boolean checkRight = varify(s.right, t.right);
        return checkLeft && checkRight;
    }
}
