/*
    ( ( )
    0 1 2
    when at index 2, we pop out 1 at stack, res should be 2 - 0(stack.peek())
*/
class Solution {
    public int longestValidParentheses(String s) {
        if(s == null || s.length() < 2) return 0;
        int res = 0, leftMost = -1;
        //stack mark the index
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '(') {
                stack.push(i);
            } else {   // )
                //start with ), new ( - last ) or -1 is length
                if(stack.isEmpty()) leftMost = i;   
                else {
                    int j = stack.pop();
                    if(stack.isEmpty()) {
                        res = Math.max(res, i - leftMost);
                    }else{
                        res = Math.max(res, i - stack.peek());
                    }
                }
            }
        }
        return res;
    }
}
