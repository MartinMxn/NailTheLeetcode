/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 
 1.find the largest, devide into two parts
 2.left:0, Lar   right:Lar+1,end
 3.left largest be the left node and right largest be the right node
 */
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if(nums == null || nums.length == 0) return null;
        //find the largest
        int index = maxIndex(nums, 0, nums.length - 1);
        TreeNode root = new TreeNode(nums[index]);
        root.left = findLargest(nums, 0, index - 1);
        root.right = findLargest(nums, index + 1, nums.length - 1);
        
        return root;
    }
    
    private TreeNode findLargest(int[] nums, int left, int right) {
        if(left <= right) {
            int index = maxIndex(nums, left, right);
            TreeNode cur = new TreeNode(nums[index]);
            cur.left = findLargest(nums, left, index - 1);
            cur.right = findLargest(nums, index + 1, right);
            return cur;
        }
        return null;
    }
    
    private int maxIndex(int[] nums, int left, int right) {
        //all initially set to right, so the left < righ would fail
        int index = right;
        int largest = nums[right];
        for(int i = left; i < right; i++) {
            if(nums[i] > largest) {
                index = i;
                largest = nums[i];
            }
        }
        return index;
    }
}
