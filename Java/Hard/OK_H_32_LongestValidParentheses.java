/*
    ( ( )
    0 1 2
    when at index 2, we pop out 1 at stack, res should be 2 - 0(stack.peek())
*/
class OK_H_32_LongestValidParentheses {
    public int longestValidParentheses(String s) {
        if(s == null || s.length() < 2) return 0;
        //position of ( )
        Stack<Integer> stack = new Stack<>();
        int res = 0, leftMost = -1;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '(') {
                stack.push(i);
            } else {
                if(stack.isEmpty()) leftMost = i;   //restart mark
                else {
                    stack.pop();    //find the second last ( or leftMost
                    if(stack.isEmpty()) {
                        res = Math.max(res, i - leftMost);
                    } else {
                        res = Math.max(res, i - stack.peek());
                    }
                }
            } 
        }
        return res;
    }
}
