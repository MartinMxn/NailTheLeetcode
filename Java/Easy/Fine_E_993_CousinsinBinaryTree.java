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
    
    class treeNode {
        TreeNode parent;
        int level;
    }
    
    public boolean isCousins(TreeNode root, int x, int y) {
        //find x and y, record parent and depth
        //return true if depth are equal and parent are dif
        
        // //1.hashmap(because it's unique value)
        // if(root == null || root.val == x || root.val == y) return false;
        // HashMap<Integer, int[]> map = new HashMap<>();
        // //node level parent map
        // dfs(root, 0, 0, map, x, y);
        // return map.get(x)[0] == map.get(y)[0] && map.get(x)[1] != map.get(y)[1];
        
        //2.customized node class
        if(root == null || root.val == x || root.val == y) return false;
        treeNode xNode = dfs2(root, x, 0, new treeNode(), root);
        treeNode yNode = dfs2(root, y, 0, new treeNode(), root);
        return xNode.parent.val != yNode.parent.val && xNode.level == yNode.level;
    }
    
    // private void dfs1(TreeNode node, int level, int parent, HashMap<Integer, int[]> map, int x, int y) {
    //     if(node == null) return;
    //     map.put(node.val, new int[]{level, parent});
    //     if(map.containsKey(x) && map.containsKey(y)) return;
    //     dfs(node.left, level + 1, node.val, map, x, y);
    //     dfs(node.right, level + 1, node.val, map, x, y);
    // }
    
    private treeNode dfs2(TreeNode node, int val, int level, treeNode tNode, TreeNode parent) {
        if(node == null) return null;
        if(node.val == val) {
            tNode.parent = parent;
            tNode.level = level;
            return tNode;
        }
        dfs2(node.left, val, level + 1, tNode, node);
        dfs2(node.right, val, level + 1, tNode, node);
        return tNode;
    }
}
