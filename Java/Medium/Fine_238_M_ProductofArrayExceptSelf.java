class Solution {
    public int[] productExceptSelf(int[] nums) {
        //1. multiple all number and divide
        
        //2. multiple and save result
        // from left to right and then left to right
        //  [1,2,3,4]
        //->[1,1,2,6]
        //  [24,12,8,6]<-
        int[] res = new int[nums.length];
        res[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        
        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= right;
            right *= nums[i];
        }
        
        return res;
    }
}
