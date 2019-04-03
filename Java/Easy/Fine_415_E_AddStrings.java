/**
 * 2345
 *  123
 take care of last remaining carry number
 */
class Solution {
    public String addStrings(String num1, String num2) {
        int carry = 0;
        int i = num1.length() - 1, j = num2.length() - 1;
        StringBuilder sb = new StringBuilder();
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if(i >= 0) {
                sum += num1.charAt(i) - '0';
                i--;
            }
            if(j >= 0) {
                sum += num2.charAt(j) - '0';
                j--;
            }
            if(sum >= 10) {
                sb.append(sum % 10);
                carry = sum / 10;
            } else {
                sb.append(sum);
                carry = 0;
            }
            
        }
        if(carry != 0) sb.append('1');  //!
        return sb.reverse().toString();
    }
}
