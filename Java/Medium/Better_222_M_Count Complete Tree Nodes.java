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
    public int countNodes(TreeNode root) {
        // 1. level order traverse and find the first node which doesn't have child
        // O(n)
        if (root == null) { return 0; }
        Queue<TreeNode> q = new LinkedList<>();
        int res = 1;
        q.offer(root);
        while(q.size() > 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode cur = q.poll();
                if (cur.left == null) return res;
                q.offer(cur.left);
                res++;
                if (cur.right == null) return res;
                q.offer(cur.right);
                res++;
            }
        }
        
        return res;
        
        // 2.find the depth and then check existence for each possible last level node
        // O(log^2 N)
           
    }
}
