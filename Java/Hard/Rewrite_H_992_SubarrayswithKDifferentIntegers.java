class Rewrite_H_992_SubarrayswithKDifferentIntegers {
    public int subarraysWithKDistinct(int[] A, int K) {
        int res = 0;
        Set<Integer> set = new HashSet<>();
        int start = 0, end = 0;
        while(end < A.length) {
            set.add(A[end]);
            if(set.size() > K) {
                set.clear();
                start++;
                end = start;
                continue;
            }
            
            if(set.size() == K) {
                res++;
                end++;
                //[1,2,1,2,1,2] K = 2
                //[  2,1,2,1,2]
                //[    1,2,1,2]
                if(end == A.length) {
                    set.clear();
                    start++;
                    end = start;
                }
                continue;
            }
            
            end++;
        }
        return res;
    }
}
