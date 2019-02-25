/*
First one pass hard problem!
*/
class Solution {
    //O(n^3)
//     public int longestConsecutive(int[] nums) {
//         if(nums == null || nums.length == 0) return 0;
//         HashSet<Integer> set = new HashSet<>();
//         for(int i : nums) set.add(i);
//         int res = 1;
//         for(int i = 0; i < nums.length; i++) {
//             if(set.contains(nums[i] - 1)) {
//                 res = Math.max(res, count(set, nums[i]));
//             }
//         }
//         return res;
//     }
    
//     private int count(HashSet<Integer> set, int num) {
//         if(!set.contains(num)) return 0;
//         return 1 + count(set, num - 1);
//     }
    
    //O(n) only start from the minimum one
    public int longestConsecutive(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        HashSet<Integer> set = new HashSet<>();
        for(int i : nums) set.add(i);
        int res = 1;
        for(int num : nums) {
            if(!set.contains(num - 1)) {
                int cur = num, count = 1;
                while(set.contains(cur + 1)) {  //only once
                    cur++;
                    count++;
                }
                res = Math.max(count, res);
            }
        }
        //O(n + n)
        return res;
    }
}
