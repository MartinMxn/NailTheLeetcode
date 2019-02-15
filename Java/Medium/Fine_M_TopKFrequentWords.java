class Fine_M_TopKFrequentWords {
    public List<String> topKFrequent(String[] words, int k) {
        //hashmap
        //O(nlogn)
        //O(n)
        // Map<String, Integer> map = new HashMap<>();
        // for(String s : words) {
        //     map.put(s, map.getOrDefault(s, 0) + 1);
        // }
        // List<String> list = new ArrayList(map.keySet());
        // //b - a ascending order
        // Collections.sort(list, (a,b) -> map.get(a).equals(map.get(b)) ?
        //                  a.compareTo(b) : map.get(b) - map.get(a)
        //                 );
        // return list.subList(0, k);
        
        //hashmap + heap
        //O(nlogk)
        //O(n)
        HashMap<String, Integer> map = new HashMap<>();
        for(String word : words) map.put(word, map.getOrDefault(word, 0) + 1);
        
        PriorityQueue<String> pq = new PriorityQueue<>(k, (a, b) 
                                                       -> map.get(a) == map.get(b) 
                                                       ? b.compareTo(a) : map.get(a) - map.get(b));
        for(String s : map.keySet()) {
            pq.add(s);
            if(pq.size() > k) {
                pq.poll();
            }
        }
        
        List<String> res = new ArrayList<>();
        while(!pq.isEmpty()) res.add(pq.poll());
        Collections.reverse(res);  //!!
        return res;
    }
}
