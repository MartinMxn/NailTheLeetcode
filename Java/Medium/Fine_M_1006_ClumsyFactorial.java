class Solution {
    public int clumsy(int N) {
        if(N == 0) return 0;
        else if(N == 1) return 1;
        else if(N == 2) return 2;
        else if(N == 3) return 6;
        else if(N == 4) return 7;
        return N * (N - 1) / (N - 2) + (N - 3) + helper(N - 4);       
    }
    
    private int helper(int N) {
        if(N == 0) return 0;
        else if(N == 1) return -1;  // -1
        else if(N == 2) return -2;  // -2 * 1
        else if(N == 3) return -6;  // -3 * 2 / 1
        else if(N == 4) return -5; // -4 * 3 / 2 + 1
        return -N * (N - 1) / (N - 2) + (N - 3) + helper(N - 4);
    }
}
