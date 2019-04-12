//sorted arr
//find right place to insert
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int index = 0;
        for (int num : nums) {
            int i = 0, j = index;
            while (i != j) {
                int mid = i + (j - i) / 2;
                // 1 4 6  :5
                if (tails[mid] < num) {
                    i = mid + 1;
                } else { //if larger or equal, then replace it
                    j = mid;
                }
            }
            tails[i] = num;
            //if i(index) = size, add at index and move to next position
            if (i == index) {
                index++;
            }
        }
        return index;
    }
}
