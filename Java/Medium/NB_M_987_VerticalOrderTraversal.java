/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//TreeMap cause x and y will automatically sorted
class NB_M_987_VerticalOrderTraversal {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        //x -> (y -> list)
        TreeMap<Integer, TreeMap<Integer, TreeSet<Integer>>> map = new TreeMap<>();
        dfs(root, 0, 0, map);
        List<List<Integer>> list = new ArrayList<>();
        for(TreeMap<Integer, TreeSet<Integer>> y : map.values()) {
            list.add(new ArrayList<>());
            for(TreeSet<Integer> set : y.values()) {
                for(int i : set) {
                    list.get(list.size() - 1).add(i);
                }
            }
        }
        return list;
    }
    
    private void dfs(TreeNode root, int x, int y, TreeMap<Integer, TreeMap<Integer, TreeSet<Integer>>> map) {
        if(root == null) return;
        if(!map.containsKey(x)) map.put(x, new TreeMap<>());
        if(!map.get(x).containsKey(y)) map.get(x).put(y, new TreeSet<>());
        map.get(x).get(y).add(root.val);
        dfs(root.left, x - 1, y + 1, map);
        dfs(root.right, x + 1, y + 1, map);
    }
}
