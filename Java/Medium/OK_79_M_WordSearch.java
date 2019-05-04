//1.find the strat character
//2.find whether the word exist in the 2D grid
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (check(board, word, i, j, 0, new boolean[m][n])) return true;
            }
        }
        
        return false;
    }
    
    private boolean check(char[][] board, String word, int i, int j, int index, boolean[][] visited) {
        int m = board.length, n = board[0].length;
        if (index == word.length()) return true;
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] ||board[i][j] != word.charAt(index)) return false;
        visited[i][j] = true;
        if (check(board, word, i + 1, j, index + 1, visited) 
            || check(board, word, i - 1, j, index + 1, visited) 
            || check(board, word, i, j + 1, index + 1, visited) 
            || check(board, word, i, j - 1, index + 1, visited)) return true; 
        visited[i][j] = false;
        return false;
    }
}
