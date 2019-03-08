/*
find firstSmall one(smaller than next one) and then
find the firstLarge one(larger than firstSmall)
swap them
and reverse the index to end from firstSmall one
1 2 7 4 3 1
  ^ 
1 2 7 4 3 1
        ^ 
1 3 7 4 2 1

1 3 1 2 4 7
*/
class Solution {
    public void nextPermutation(int[] nums) {
        if(nums == null || nums.length < 2) return;
        
        int firstSmall = -1;
        //find the last ascending one
        //from - 2 cause comparsion needs i + 1
        for(int i = nums.length - 2; i >=0; i--) {
            if(nums[i] < nums[i + 1]) {
                firstSmall = i;
                break;
            }
        }
        
        if(firstSmall == -1) {
            reverse(nums, 0, nums.length);
            return;
        }
        
        int firstLarge = -1;
        for(int i = nums.length - 1; i > firstSmall; i--) {
            if(nums[i] > nums[firstSmall]) {
                firstLarge = i;
                break;
            }
        }
        
        //swap firstSmall firstLarge
        swap(nums, firstSmall, firstLarge);
        reverse(nums, firstSmall + 1, nums.length - 1);
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    public void reverse(int[] nums, int i, int j) {
        while(i < j) {
            swap(nums, i++, j--);
        }
    }
}
