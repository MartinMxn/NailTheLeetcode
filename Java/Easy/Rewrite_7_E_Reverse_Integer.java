class Solution {
    public int reverse(int x) {
        int flag = x < 0 ? -1 : 1;
        int res = 0;
        x = Math.abs(x);
        
        while (x > 0) {
            if (res > Integer.MAX_VALUE / 10 || (res * 10 + x % 10) > Integer.MAX_VALUE){
                return 0;
            }
            res = (x % 10) + res * 10;
            x /= 10;
        }
        
        return res * flag;
    }
}
