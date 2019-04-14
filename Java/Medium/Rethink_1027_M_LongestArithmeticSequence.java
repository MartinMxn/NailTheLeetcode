class Solution {
    /*
        [20,1,15,3,10,5,6]
        
     */
    public int longestArithSeqLength(int[] A) {
        //A[i]->(diff->length)
        HashMap<Integer, Map<Integer, Integer>> map = new HashMap<>();
        int res = 0;
        for (int i = 0; i < A.length; i++) {
            map.put(A[i], new HashMap<>());
            for (int j = 0; j < i; j++) {
                int diff = A[i] - A[j];
                Map<Integer, Integer> prev = map.get(A[j]);
                if (prev.containsKey(diff)) {
                    map.get(A[i]).put(diff, prev.get(diff) + 1);
                } else {
                    map.get(A[i]).put(diff, 2);
                }
                res = Math.max(res, map.get(A[i]).get(diff));
            }
        }
        return res;
    }
}
