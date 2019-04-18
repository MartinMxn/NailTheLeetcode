class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        //map to record the frequency
        //then priorityqueue to find the top K frequent numbers
        //O(nlogk)
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int i : nums) {
            freq.put(i, freq.getOrDefault(i, 0) + 1);
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(k, (a,b) -> freq.get(a) - freq.get(b));
        List<Integer> res = new ArrayList<>();
        for (int i : freq.keySet()) {
            pq.offer(i);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        int size = pq.size();
        for (int i = 0; i < size; i++) {
            res.add(0, pq.poll());
        }
        return res;
    }
}
