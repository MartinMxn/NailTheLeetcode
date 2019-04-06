class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        permutation(nums, res, new LinkedList<Integer>(), new boolean[nums.length]);
        return res;
    }
    
    private void permutation(int[] nums, List<List<Integer>> res, LinkedList<Integer> cur, boolean[] visited) {
        if (cur.size() == nums.length) {
            res.add(new LinkedList<Integer>(cur));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!visited[i]) {
                cur.add(nums[i]);
                visited[i] = true;
                permutation(nums, res, cur, visited);
                cur.remove(cur.size() - 1);
                visited[i] = false;
            }
        }
    }
}
