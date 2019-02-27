class Solution {
//     public int singleNumber(int[] nums) {
//         int one = 0, two = 0, three = 0;
//         for(int i : nums) {
//             // pass one to two and hold
//             two |= one & i;
//             //one is number appers once
//             one ^= i;
//             //appears three times
//             three = one & two;
            
//             //if one has three, means it has three times
//             //clear the three in one and two
//             one &= ~three;
//             two &= ~three;
//         }
//         return one;
//     }
    
    //1 ()() 1 ()() 1 == 0
    //the operator should be add all number in this bit and % 3
    public int singleNumber(int[] nums) {
        if(nums.length == 1) return nums[0];
        //mask here is decimal 1, so is 0000 0000 0000 0001 in binary
        //and any number & 1 is the last bit of the number
        int res = 0, mask = 1;
        for(int i = 0; i < 32; i++) {
            int sum = 0;
            for(int num : nums) {
                //move i, get i bit of this number
                sum += (num >> i) & mask;
                sum %= 3;
            }
            //recover
            res = res | (sum << i); 
        }
        return res;
    }

}
