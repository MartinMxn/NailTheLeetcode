class Solution {
    public String multiply(String num1, String num2) {
        if (num1.length() == 0 || num2.length() == 0) return "0";
        int len1 = num1.length();
        int len2 = num2.length();
        int[] res = new int[len1 + len2];
        // 12
        // 34
        // 0 0 0 0
        //       8
        //     
        for (int i = len1 - 1; i >= 0; i--) {
            for (int j = len2 - 1; j >= 0; j--) {
                int mulitiple = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                int posLow = i + j + 1;
                int posHigh = i + j;
                mulitiple += res[posLow];
                res[posLow] = mulitiple % 10;
                res[posHigh] += mulitiple / 10;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for(int num : res) {
            if( !(num == 0 && sb.length() == 0 )) sb.append(num);
        }
        
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
