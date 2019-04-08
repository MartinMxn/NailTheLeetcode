class Solution {
    public int rob(int[] nums) {
        int len = nums.length;
        if (len == 0) return 0;
        if (len == 1) return nums[0];
        int[] r_rf = new int[len];
        int[] r_nf = new int[len];
        int[] n_rf = new int[len];
        int[] n_nf = new int[len];
        r_rf[0] = nums[0];
        r_nf[0] = 0;
        n_rf[0] = 0;
        n_nf[0] = 0;
        for (int i = 1; i < len; i++) {
            r_rf[i] = n_rf[i - 1] + nums[i];
            r_nf[i] = n_nf[i - 1] + nums[i];
            n_nf[i] = Math.max(n_nf[i - 1], r_nf[i - 1]);
            n_rf[i] = Math.max(n_rf[i - 1], r_rf[i - 1]);
        }
        int res = Math.max(r_nf[len - 1], n_rf[len - 1]);
        // no need to compare n_nf, it's must smaller than n_rf
        return res;
    }
}
