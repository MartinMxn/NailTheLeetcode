//find the border O, mark it as B
//then fill the other O
class OK_130_M_SurroundedRegions {
    public void solve(char[][] board) {
        if(board.length == 0 || board[0].length == 0) return;
        int m = board.length, n = board[0].length;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == 'O' && (i == 0 || i == m - 1 || j == 0 || j == n - 1)) 
                    dfs(board, i, j);
            }
        }
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == 'O') 
                    board[i][j] = 'X';
                if(board[i][j] == 'B')
                    board[i][j] = 'O';
            }
        }
    }
    
    public void dfs(char[][] board, int x ,int y) {
        int m = board.length, n = board[0].length;
        if(x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'O') {
            board[x][y] = 'B';
            dfs(board, x + 1, y);
            dfs(board, x - 1, y);
            dfs(board, x, y + 1);
            dfs(board, x, y - 1); 
        }
    }
}
