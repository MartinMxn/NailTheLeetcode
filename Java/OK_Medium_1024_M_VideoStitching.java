//greedy to maintain the max
//find the max end one in range and count
class Solution {
    public int videoStitching(int[][] clips, int T) {
        Arrays.sort(clips, (a, b) -> {
            return a[0] - b[0];
        });
        int res = 0;
        int max = 0;
        int i = 0;
        while (i < clips.length) {
            if (clips[i][0] > max) return -1;
            
            int curMax = max;
            while (i < clips.length && clips[i][0] <= curMax) {
                max = Math.max(max, clips[i][1]);
                i++;
            }
            res++;
            if(max >= T) return res;
        }
        return -1;
    }
}
