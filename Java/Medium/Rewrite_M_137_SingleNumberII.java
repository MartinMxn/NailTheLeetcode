class Solution {
    public int singleNumber(int[] nums) {
        int one = 0, two = 0, three = 0;
        for(int i : nums) {
            // pass one to two and hold
            two |= one & i;
            //one is number appers once
            one ^= i;
            //appears three times
            three = one & two;
            
            //if one has three, means it has three times
            //clear the three in one and two
            one &= ~three;
            two &= ~three;
        }
        return one;
    }
}
