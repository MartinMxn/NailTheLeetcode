/*
even num: 1-2-3-4
return 2-3
odd num 1-2-3
return 2
so remove the leaf node until left one or two ode
*/
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<List<Integer>>();
        List<Integer> res = new ArrayList<>();
        if(n == 1) {
            res.add(0);
            return res;
        }
        int[] degree = new int[n];
        for(int i = 0; i < n; i++) graph.add(new ArrayList<Integer>());
        
        for(int i = 0; i < edges.length; i++) {
            int a = edges[i][0], b = edges[i][1];
            graph.get(a).add(b);
            graph.get(b).add(a);
            degree[a]++;
            degree[b]++;
        }
        
        Queue<Integer> leaf = new LinkedList<>();
        
        //find left node
        for(int i = 0; i < n; i++) {
            if(degree[i] == 0) return res;
            else if (degree[i] == 1) {
                leaf.offer(i);
            }
        }
        
        while(!leaf.isEmpty()) {
            res = new ArrayList<Integer>();
            int count = leaf.size();
            for(int i = 0; i < count; i++) {
                int cur = leaf.poll();
                res.add(cur);
                degree[cur]--;
                for(int j = 0; j < graph.get(cur).size(); j++) {
                    int next = graph.get(cur).get(j);
                    if(degree[next] == 0) continue;
                    if(degree[next] == 2) leaf.offer(next); //find next turn leaf node
                    degree[next]--;
                }
            }
        }
        return res;
    }
    
}
