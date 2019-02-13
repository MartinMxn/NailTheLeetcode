//care about "]" / "["

class OK_E_20_ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for(char c : s.toCharArray()) {
            if(c == '{' || c == '[' || c == '(') stack.push(c);
            else {
                if(stack.isEmpty()) return false;
                char last = stack.pop();
                if(last == '{' && c != '}' ||
                  last == '[' && c != ']' ||
                  last == '(' && c != ')')
                    return false;
            }
        }
        
        return stack.isEmpty() ? true : false;
    }
}
