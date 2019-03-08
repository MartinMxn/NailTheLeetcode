/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 recursion with 3 arguments result list, current node, and depth
 if depth == result.size() we add current node to it
 and we always add the right node first, in this way the left node with same depth will not be added
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null) return res;
        addNode(res, root, 0);
        return res;
    }
    
    private void addNode(List<Integer> res, TreeNode cur, int curDepth) {
        if(cur != null) {
            if(curDepth == res.size()){
                res.add(cur.val);
            }
            //always right first to make sure right view 
            addNode(res, cur.right, curDepth + 1);
            addNode(res, cur.left, curDepth + 1);
        }
    }
}
