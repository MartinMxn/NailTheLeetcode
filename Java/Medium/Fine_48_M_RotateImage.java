/*
    1  2  3  4      
    5  6  7  8
    9  10 11 12
    13 14 15 16
         |
         |first
    -----
      i - first
    top = matrix[first][i];
    left = matrix[last - i + first][first];
    bottom = matrix[last][last - i + first];
    right = matrix[i][last];
    
*/

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int layer = 0; layer < n / 2; layer++) {
            int first = layer;
            int last = n - 1- layer;
            for (int i = first; i < last; i++) {
                // System.out.println("first:" + first + " i:" + i + " last:" + last);
                // System.out.println("top:" + matrix[first][i]);
                // System.out.println("left:" + matrix[first][i]);
                // System.out.println("bottom:" + matrix[first][i]);
                // System.out.println("right:" + matrix[first][i]);
                int top = matrix[first][i];
                //top <- left
                matrix[first][i] = matrix[last - (i - first)][first];
                //left <- bottom
                matrix[last - (i - first)][first] = matrix[last][last - (i - first)];
                //bottom <- right
                matrix[last][last - (i - first)] = matrix[i][last];
                //right <- top
                matrix[i][last] = top;
            }
        }
    }
}
