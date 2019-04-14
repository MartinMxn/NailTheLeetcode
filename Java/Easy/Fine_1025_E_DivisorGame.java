class Solution {
    public boolean divisorGame(int N) {
        if (N == 1) return false;
        if (N == 2) return true;
        if (N == 3) return false;
        if (N == 4) return true;
        
        if (N == 5) return false;
        if (N == 6) return true;
        
        return N % 2 == 0;
    }
}
