/*
[0,0,0,0]
[1,0,1,0]
[0,1,1,0]
[0,0,0,0]
*/
class Solution {
    public int numEnclaves(int[][] A) {
        int m = A.length, n = A[0].length;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                    if(A[i][j] == 1) {
                        DFS(A, i, j);
                    }
                }
            }
        }
        int res = 0;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) { 
                if(A[i][j] == 1) res++;   
            }
        }
        return res;
    }
    
    private void DFS(int[][]A, int i, int j) {
        int m = A.length, n = A[0].length;
        if( i < 0 || i > m - 1 || j < 0 || j > n - 1 || A[i][j] == 0) return;
        A[i][j] = 0;
        DFS(A, i + 1, j);
        DFS(A, i - 1, j);
        DFS(A, i, j + 1);
        DFS(A, i, j - 1);
    }
}
