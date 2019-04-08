//from the left, check palindrome for both odd and even each time
//gloval variable to record the max result
class Solution {
    String res = "";
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) return "";
        for (int i = 0; i < s.length(); i++) {
            // s, left, right
            calcu(s, i, i);
            calcu(s, i, i + 1);
        }
        return res;
    }
    
    private void calcu(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        String tmp = s.substring(left + 1, right);
        if (tmp.length() > res.length()) res = tmp;
    }
}
