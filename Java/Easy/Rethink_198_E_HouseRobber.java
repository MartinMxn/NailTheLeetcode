class Solution {
    public int rob(int[] nums) {
        //dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1])
        int len = nums.length;
        if(nums == null || len == 0) return 0;
        int[] rub = new int[len];
        int[] norub = new int[len];
        rub[0] = nums[0];
        norub[0] = 0;
        for (int i = 1; i < len; i++) {
            rub[i] = norub[i - 1] + nums[i];
            norub[i] = Math.max(rub[i - 1], norub[i - 1]);
        }
        return Math.max(rub[len - 1], norub[len - 1]);
    }
}
