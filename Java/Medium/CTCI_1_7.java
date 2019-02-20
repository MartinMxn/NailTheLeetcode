/*
* rotate the NxN matrix by 90 degrees
* */
class CTCI_1_7 {
    /*
    *
    * 1 2 3 4
    * 2 1 1 3
    * 3 1 1 2
    * 4 3 2 1
    *
    * 1<->4
    * 2<->3
    *
    * */
    public void rotate(int[][] matrix) {
         int n = matrix.length;
         for(int layer = 0; layer < n; layer++) {
             int first = layer;
             int last = n - 1 - layer;
             for(int i = first; i < last; i++) {
                 int offset = i - first;
                 // left matrix[last - offset][first]
                 // top matrix[first][i]
                 // right matrix[last][last - offset]
                 // bottom matrix[i][last]
                 int top = matrix[first][i];
                 //left -> top
                 matrix[first][i] = matrix[last - offset][first];
                 //bottom -> left
                 matrix[last - offset][first] = matrix[last][last - offset];
                 //right -> bottom
                 matrix[last][last - offset] = matrix[i][last];
                 //top -> right
                 matrix[i][last] = top;
             }
         }
    }
}
