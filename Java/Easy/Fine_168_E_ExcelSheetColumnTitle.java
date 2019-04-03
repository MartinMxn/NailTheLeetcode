//think from ASCII 
//10-base to 26-base
class Solution {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            //n -- to make it from 0, not 1
            n--;
            sb.append((char)('A' + n % 26));
            n /= 26;
        }
        return sb.reverse().toString();
    }
}
