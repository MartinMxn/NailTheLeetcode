//stack
// (())
class Solution {
    public String removeOuterParentheses(String S) {
        Stack<Character> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (char c : S.toCharArray()) {
            if (c == '(' && stack.size() == 0) {
                stack.push(c);  //might be just ()
            } else if (c == '(' && stack.size() >= 1) {
                stack.push(c);
                sb.append('(');
            } else if (c == ')' && stack.size() == 1) {
                stack.pop();
            } else if (c == ')' && stack.size() > 1) {
                stack.pop();
                sb.append(')');
            }
        }
        return sb.toString();
    }
}
