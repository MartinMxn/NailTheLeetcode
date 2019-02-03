//take care of input length
class Solution {
    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {
        int[] res = new int[A.length];
        for(int i = 0; i < queries.length; i++){
            A[queries[i][1]] += queries[i][0];
            res[i] = sum(A);
        }
        return res;
    }
    
    public int sum(int[] A){
        int res = 0;
        for(int i = 0; i < A.length; i++){
            if(A[i] % 2 == 0) res += A[i];
        }
        return res;
    }
}
