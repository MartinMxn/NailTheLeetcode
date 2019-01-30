package Java.Hard;/*
  0 1 2 3 4 5
0 
1
2
3
4
replace | insert
-----------------
delete  | dp[i][j]
if charAt(i) == charAt(j) dp[i][j] = min of 3 operations
if charAt(i) != charAt(j) dp[i][j] = 1 + min of 3 operations
*/

class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        //state distance between word1[x] and word2[y];
        int[][] dp = new int[len1 + 1][len2 + 1];
        //init
        for(int i = 0; i <= len1; i++) dp[i][0] = i;
        for(int i = 0; i <= len2; i++) dp[0][i] = i;
        /*
            function if[i] == [j] 
            dp[i][j] = min(1 + dp[i - 1][j], 1 +dp[i][j - 1], dp[i - 1][j - 1])
            else
            dp[i][j] = min(1 + dp[i - 1][j], 1 +dp[i][j - 1], 1 + dp[i - 1][j - 1])
        */
        for(int i = 1; i <= len1; i++){
            for(int j = 1; j <= len2; j++){
                //init for each grid 
                dp[i][j] = Integer.MAX_VALUE;
                if(word1.charAt(i - 1) == word2.charAt(j - 1)){
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
                    dp[i][j] = Math.min(dp[i][j], dp[i -1][j - 1]);
                }else{
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
                    dp[i][j] = Math.min(dp[i][j], 1 + dp[i -1][j - 1]);
                }
            }
        }
        return dp[len1][len2];
    }
}