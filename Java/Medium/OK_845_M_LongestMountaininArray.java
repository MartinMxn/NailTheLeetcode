class Solution {
    public int longestMountain(int[] A) {
        int max = 0;
        if (A == null || A.length < 3) return 0;
        for (int i = 1; i < A.length - 1; i++) {
            if (A[i - 1] < A[i] && A[i] > A[i + 1]) {
                int left = i - 1;
                int right = i + 1;
                while (left >= 0  
                      && A[left] < A[left + 1]) {
                    left--;
                }
                while (right < A.length && A[right] < A[right - 1] ) {
                    right++;
                }
                max = Math.max(max, right - left - 1);
            }
        }
        return max;
    }
}
