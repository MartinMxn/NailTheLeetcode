class Solution {
    // public List<Integer> topKFrequent(int[] nums, int k) {
    //     //map to record the frequency
    //     //then priorityqueue to find the top K frequent numbers
    //     //O(nlogk)
    //     HashMap<Integer, Integer> freq = new HashMap<>();
    //     for (int i : nums) {
    //         freq.put(i, freq.getOrDefault(i, 0) + 1);
    //     }
    //     PriorityQueue<Integer> pq = new PriorityQueue<>(k, (a,b) -> freq.get(a) - freq.get(b));
    //     List<Integer> res = new ArrayList<>();
    //     for (int i : freq.keySet()) {
    //         pq.offer(i);
    //         if (pq.size() > k) {
    //             pq.poll();
    //         }
    //     }
    //     int size = pq.size();
    //     for (int i = 0; i < size; i++) {
    //         res.add(0, pq.poll());
    //     }
    //     return res;
    // }
    
    //bucket sort
    //List<Integer>[] bucket !
    //O(n)
    public List<Integer> topKFrequent(int[] nums, int k) {
        //record freq
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        //add to bucket
        //bucket[freq] = num
        List<Integer>[] bucket = new List[nums.length + 1];
        for (int key : map.keySet()) {
            int freq = map.get(key);
            if (bucket[freq] == null) {
                bucket[freq] = new ArrayList<>();
            }
            bucket[freq].add(key);
        }
        
        List<Integer> res = new ArrayList<>();
        for (int i = bucket.length - 1; i >= 0 && res.size() < k; i--) {
            if (bucket[i] != null) {
                res.addAll(bucket[i]);
            }
        }
        return res;
    }
}
