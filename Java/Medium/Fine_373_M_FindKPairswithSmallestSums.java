class Solution {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<int[]> res = new ArrayList<>();
        if (nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0) return res;
        PriorityQueue<int[]> pq = new PriorityQueue<>(k, (int[] a, int[] b) -> {
            return b[0] + b[1] - a[0] - a[1];
        });
        int count = 0;
        // [2,4,8]
        // [1,3,5]
        for (int i = 0; i < nums1.length; i++) {
            if (count >= k) break;
            for (int j = 0; j < nums2.length; j++) {
                if (count >= k) break;
                pq.add(new int[]{nums1[i], nums2[j]});
                if (pq.size() > k) pq.poll();
                count++;
            }
        }
        int size = pq.size(); //!! corner case k may larger than the total paris number
        for (int i = 0; i < size; i++) res.add(pq.poll());
        return res;
    }
}
