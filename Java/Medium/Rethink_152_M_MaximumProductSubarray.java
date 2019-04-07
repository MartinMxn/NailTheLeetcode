class Solution {
    public int maxProduct(int[] nums) {
        int[] dp = new int[nums.length];
        int min = nums[0];
        int max = nums[0];
        int res = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] >= 0) {
                min = Math.min(nums[i], nums[i] * min);
                max = Math.max(nums[i], nums[i] * max);
            } else { // < 0
                int tmp = max;
                max = Math.max(nums[i], min * nums[i]);
                min = Math.min(nums[i], tmp * nums[i]);
            }
            res = Math.max(res, max);
        }
        return res;
    }
}
