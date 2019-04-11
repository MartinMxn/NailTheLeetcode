class Solution {
    //O(nlogk)
    // public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
    //     List<int[]> res = new ArrayList<>();
    //     if (nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0) return res;
    //     PriorityQueue<int[]> pq = new PriorityQueue<>(k, (int[] a, int[] b) -> {
    //         return b[0] + b[1] - a[0] - a[1];
    //     });
    //     // [2,4,8]
    //     // [1,3,5]
    //     for (int i = 0; i < nums1.length; i++) {
    //         for (int j = 0; j < nums2.length; j++) {
    //             pq.add(new int[]{nums1[i], nums2[j]});
    //             if (pq.size() > k) pq.poll();
    //         }
    //     }
    //     int size = pq.size(); //!! corner case k may larger than the total paris number
    //     for (int i = 0; i < size; i++) res.add(pq.poll());
    //     return res;
    // }
    
    //O(klogk)
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<int[]> res = new ArrayList<>();
        if (nums1 == null || nums1.length == 0 || nums2 == null || nums2.length == 0) return res;
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] num1, int[] num2) {
                int sum1 = num1[0] + num1[1];
                int sum2 = num2[0] + num2[1];
                return sum1 - sum2;
            }
        });
        //pq num in nums1, num in nums2, index of nums2
        //put all nums1 to pq(at most k)
        for (int i = 0; i < nums1.length && i < k; i++) {
            pq.add(new int[] {nums1[i], nums2[0], 0});
        }
        
        while (k-- > 0 && !pq.isEmpty()) {
            int[] num = pq.poll();
            res.add(new int[]{num[0], num[1]});
            if (num[2] < nums2.length - 1) {
                pq.add(new int[]{num[0], nums2[num[2] + 1], num[2] + 1});
            }
        }
        return res;
    }
}
