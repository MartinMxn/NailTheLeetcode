/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Fine_M_988_SmallestStringStartingFromLeaf {
    public String smallestFromLeaf(TreeNode root) {
        String[] res = new String[1];
        //root, tmp, res
        dfs(root, "", res);
        return res[0];
    }
    
    private void dfs(TreeNode root, String tmp, String[] res) {
        if(root == null) return;
        if(root.left == null && root.right == null) {
            tmp = (char) (root.val + 'a') + tmp; // ! can't be +=, it's reverse order so tmp = .. + tmp
            if(res[0] == null || tmp.compareTo(res[0]) < 0) {
                res[0] = tmp;
            }
            return;
        }
        tmp = (char)(root.val + 'a') + tmp;
        dfs(root.left, tmp, res);
        dfs(root.right, tmp, res);
    }
}
