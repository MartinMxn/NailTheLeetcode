class Solution {
    public int orangesRotting(int[][] grid) {
        //push all rotten cell into queue and count for fresh
        //expand for adjacent cell each round and return round
        int r = grid.length;
        int c = grid[0].length;
        Queue<int[]> rottenO = new LinkedList<>();
        int freshCount = 0;
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                if(grid[i][j] == 2) rottenO.offer(new int[]{i, j});
                else if(grid[i][j] == 1) freshCount++;
            }
        }
        
        if(freshCount == 0) return 0;
        int round = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while(!rottenO.isEmpty() && freshCount > 0) {
            round++;
            int size = rottenO.size();
            for(int i = 0; i < size; i++) {
                int[] cell = rottenO.poll();
                for(int[] dir : dirs) {
                    int x = cell[0] + dir[0];
                    int y = cell[1] + dir[1];
                    if(x >= 0 && x < r && y >=0 && y < c && grid[x][y] == 1) {
                        rottenO.offer(new int[]{x, y});
                        grid[x][y] = 2;
                        freshCount--;
                    }
                }
            }
        }
        return freshCount == 0 ? round : -1;
    }
}
