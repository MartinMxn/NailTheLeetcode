class Fine_200_NumberofIslands {
    //BFS
//     public int numIslands(char[][] grid) {
//         if(grid.length == 0 || grid[0].length == 0) return 0;
//         int m = grid.length, n = grid[0].length, res = 0;
//         for(int i = 0; i < m; i++) {
//             for(int j = 0; j < n; j++) {
//                 if(grid[i][j] == '1') {
//                     expand(grid, i, j);
//                     res++;
//                 }
//             }
//         }
//         return res;
//     }
    
//     private void expand(char[][] grid, int x, int y) {
//         int m = grid.length, n = grid[0].length;
//         if(x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == '1') {
//             grid[x][y] = '2';
//             expand(grid, x + 1, y);
//             expand(grid, x - 1, y);
//             expand(grid, x, y + 1);
//             expand(grid, x, y - 1);
//         }
//     }
    
    //Union find
    public int numIslands(char[][] grid) {
        if(grid.length == 0 || grid[0].length == 0) return 0;
        int m = grid.length, n = grid[0].length, res = 0;
        UnionFind uf = new UnionFind(grid);
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == '1') {
                    int p = i * n + j;
                    int q;
                    //up
                    if(i > 0 && grid[i - 1][j] == '1') {
                        /*  1
                            1 ⬆️  
                           q =  p - n
                        */
                        q = p - n;
                        uf.union(p, q);
                    }
                    //down
                    if(i < m - 1 && grid[i + 1][j] == '1') {
                        q = p + n;
                        uf.union(p, q);
                    }
                    if(j > 0 && grid[i][j - 1] == '1') {
                        q = p - 1;
                        uf.union(p, q);
                    }
                    if(j < n - 1 && grid[i][j + 1] == '1') {
                        q = p + 1;
                        uf.union(p, q);
                    }
                }
            }
        }
        return uf.count;
    }
    
    class UnionFind {
        int[] union;
        int m, n, count;
        UnionFind(char[][] grid) {
            m = grid.length;
            n = grid[0].length;
            union = new int[m*n];
            for(int i = 0; i < m; i++) {
                for(int j = 0; j < n; j++) {
                    if(grid[i][j] == '1') {
                        count++;
                        union[i * n + j] = i * n + j;
                    }
                }
            }
        }
        
        public void union(int index1, int index2) {
            int find1 = find(index1), find2 = find(index2);
            if(find1 != find2) {
                union[find1] = find2;
                count--;
            }
        }
        
        public int find(int x) {
            if(union[x] != x) x = find(union[x]);
            return x;
        }
    }
}
