/*
Cut Leaf Node

go through all the pairs build graph
save it as List<List<Integer>>
and calculate the degree of each node

find the leaf node and remove with q
until we got one or two root node
*/
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> res = new ArrayList<>();
        List<List<Integer>> graph = new ArrayList<>();
        int[] degree = new int[n];
        //if only contains one node it should return 0, cause it start from 0
        if(n == 1) {
            res.add(0);
            return res;
        }
        
        //iterate pair and build graph
        for(int i = 0; i < n; i++) graph.add(new ArrayList<Integer>());
        for(int[] pair : edges) {
            int a = pair[0], b = pair[1];
            graph.get(a).add(b);
            graph.get(b).add(a);
            degree[a]++;
            degree[b]++;
        }
        
        //cut the leaf node
        Queue<Integer> leaf = new LinkedList<>();
        for(int i = 0; i < n; i++) {
            if(degree[i] == 1) leaf.offer(i);
        }
        
        while(!leaf.isEmpty()) {
            res = new ArrayList<>();
            int size = leaf.size();
            for(int i = 0; i < size; i++) {
                int cur = leaf.poll();
                //for last root 
                res.add(cur);
                degree[cur]--;
                for(int j = 0; j < graph.get(cur).size(); j++) {
                    int connected = graph.get(cur).get(j);
                    if(degree[connected] == 0) continue;
                    if(degree[connected] == 2) {
                        leaf.offer(connected);
                    }
                    degree[connected]--;
                }
            }
        }
        
        return res;
    }
}
