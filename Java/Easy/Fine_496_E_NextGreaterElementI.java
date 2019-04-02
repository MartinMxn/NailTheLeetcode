//because the number in num1 and num2 are UNIQUE
//could use monolitic stack to find next larger oen and hashmap to store result
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] res = new int[nums1.length];
        Arrays.fill(res, -1);
        HashMap<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for(int i = nums2.length - 1; i >= 0; i--) {
            while(!stack.isEmpty() && stack.peek() < nums2[i]) {
                stack.pop();
            } 
            if(!stack.isEmpty()) map.put(nums2[i], stack.peek());
            stack.push(nums2[i]);
        }
        for(int i = 0; i < nums1.length; i++) {
            if(map.get(nums1[i]) != null) res[i] = map.get(nums1[i]); 
        }
        return res;
    }
}
