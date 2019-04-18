class Solution {
    public void sortColors(int[] nums) {
        if(nums == null || nums.length == 0) return;
        int left = 0;
        int right = nums.length - 1;
        int index = 0;
        //red, white, and blue
        //[2, 0, 1]
        while (index <= right) {
            if (nums[index] == 0) {
                swap(nums, index++, left++);
            } else if (nums[index] == 1) {
                index++;
            } else { // 2
                swap(nums, index, right--); 
                //! not index++
                //cause don't know nums[right] is 0 or 1
            }
        }
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
