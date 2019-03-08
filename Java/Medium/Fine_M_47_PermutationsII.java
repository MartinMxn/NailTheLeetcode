class Solution {
    
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        boolean[] visited = new boolean[nums.length];
        ArrayList<Integer> tmpList = new ArrayList<>();
        allPermutations(res, nums, tmpList, visited);
        return res;
    }
    
    private void allPermutations(List<List<Integer>> res, int[] nums, ArrayList<Integer> tmpList, boolean[] visited) {
        if(tmpList.size() == nums.length) {
            res.add(new ArrayList<>(tmpList));
            return;
        } else {
            for(int i = 0; i < nums.length; i++) {
                if(visited[i] || (i > 0 && !visited[i - 1] && nums[i] == nums[i - 1])) {
                    continue;
                } else {
                    tmpList.add(nums[i]);
                    visited[i] = true;
                    // System.out.println(nums[i]);
                    allPermutations(res, nums, tmpList, visited);
                    tmpList.remove(tmpList.size() - 1);
                    visited[i] = false;
                }
            }
        }
    }
}
