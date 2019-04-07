class Solution {
    public int videoStitching(int[][] clips, int T) {
        Arrays.sort(clips, (int[]a, int[]b) -> {
            return a[0] - b[0];
        });
        int count = 0;
        int max = 0;
        int i = 0;
        while (i < clips.length) {
            if (clips[i][0] > max) {
                return -1;
            }
            
            int curMax = max;
            while (i < clips.length && clips[i][0] <= max) {
                curMax = Math.max(curMax, clips[i][1]);
                i++;
            }
            
            max = curMax;
            count++;
            if(max >= T) return count;
        }
        
        return -1;
    }
}
