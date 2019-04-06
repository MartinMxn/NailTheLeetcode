class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        permutation(nums, res, new ArrayList<Integer>(), new boolean[nums.length]);
        return res;
    }
    
    private void permutation(int[] nums, List<List<Integer>> res, List<Integer> tmp, boolean[] visited) {
        if (tmp.size() == nums.length) {
            res.add(new ArrayList<>(tmp)); //give it a new address, when remove would not effect 
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if(visited[i] || (i > 0 && !visited[i - 1] && nums[i] == nums[i - 1])) continue;
            visited[i] = true;
            tmp.add(nums[i]);
            permutation(nums, res, tmp, visited);
            tmp.remove(tmp.size() - 1);
            visited[i] = false;
        }
    }
}
