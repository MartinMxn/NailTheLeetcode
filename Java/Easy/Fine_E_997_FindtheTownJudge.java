/*
every one trust the judge so the judge is the one who go through N - 1 times
*/
class Solution {
    public int findJudge(int N, int[][] trust) {
        int[] count = new int[N + 1];
        for(int[] pair : trust) {
            count[pair[0]]--;
            count[pair[1]]++;
        }
        
        for(int i = 1; i <= N; i++) {
            if(count[i] == N - 1) return i;
        }
        
        return -1;
    }
}
