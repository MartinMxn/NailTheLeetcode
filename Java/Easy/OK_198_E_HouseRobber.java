/*dp
  1,2,3,4,5
      ^
      rub -> norub + nums[i]
      or
      norub -> max(norub(i - 1), rub(i - 1))
*/
class Solution {
    public int rob(int[] nums) {
        int len = nums.length;
        if(len == 0) return 0;
        int[] rub = new int[len];
        int[] norub = new int[len];
        rub[0] = nums[0];
        norub[0] = 0;
        for (int i = 1; i < len; i++) {
            rub[i] = norub[i - 1] + nums[i];
            norub[i] = Math.max(norub[i - 1], rub[i - 1]);
        }
        return Math.max(rub[len - 1], norub[len - 1]);
        
        /*
        int rub = nums[0];
        int norub = 0;
        for (int i = 1; i < len; i++) {
            int prevRub = rub;
            rub = norub + nums[i];
            norub = Math.max(norub, prevRub);
        }
        return Math.max(rub, norub);
        */
    }
}
