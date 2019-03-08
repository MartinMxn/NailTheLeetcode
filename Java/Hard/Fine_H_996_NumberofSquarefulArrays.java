//try all the permutation, if last one and cur one sum up to a perfect square, add to tmpList
//set the visited[i] to true, and recursion, after that backtrack the visited and list
//if the length of tmpList is equal to A.length, add 1 to res
class Solution {
    public int numSquarefulPerms(int[] A) {
        Arrays.sort(A);
        return backtrack(A, 0, new ArrayList<Integer>(), new boolean[A.length]);
    }
    
    private int backtrack(int[] A, int res, ArrayList<Integer> tmpList, boolean[] visited) {
        if(tmpList.size() == A.length) {
            return ++res;
        } else {
            for(int i = 0; i < A.length; i++) {
                if(visited[i]
                  || i > 0  && (A[i - 1] == A[i] && !visited[i - 1])
                  || tmpList.size() >0 && !isSquareful(tmpList.get(tmpList.size() -1), A[i]) ) {
                    continue;
                } else {
                    visited[i] = true;
                    tmpList.add(A[i]);
                    // System.out.println(A[i]);
                    res = backtrack(A, res, tmpList, visited);
                    visited[i] = false;
                    tmpList.remove(tmpList.size() - 1);
                }
            }
        }
        return res;
    }
    
    private boolean isSquareful(int a, int b) {
        double sqrt = Math.sqrt(a + b);
        //cant (int)(sqrt * sqrt)
        return (int)sqrt * sqrt == a + b;
    }
}
