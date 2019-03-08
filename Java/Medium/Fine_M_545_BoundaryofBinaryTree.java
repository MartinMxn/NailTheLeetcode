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
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root != null) {
            res.add(root.val);
            print_left(res, root.left);
            print_leaves(res, root.left);
            print_leaves(res, root.right);
            print_right(res, root.right);
        }
        return res;
    }
    
    private void print_left(List<Integer> res, TreeNode root) {
        if(root != null) {
            if(root.left != null) {
                res.add(root.val);
                print_left(res, root.left);
            } else if(root.right != null){
                res.add(root.val);
                print_left(res, root.right);
            }
        }
    }
    
    private void print_right(List<Integer> res, TreeNode root) {
        if(root != null) {
            if(root.left == null && root.right == null) return;
            if(root.right != null) print_right(res, root.right);
            else if(root.left != null) print_right(res, root.left);
            res.add(root.val); 
        }
    }
    
    private void print_leaves(List<Integer> res, TreeNode root) {
        if(root != null) {
            print_leaves(res, root.left);
            if(root.left == null && root.right == null) res.add(root.val);
            print_leaves(res, root.right);
        }
    }

}
