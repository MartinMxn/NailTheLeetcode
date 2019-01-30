package Java.Medium;

import java.util.*;

/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
//BFS
public class Rewrite_M_133_CloneGraph {

    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        //original graph to the new graph through map
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();
        if(node == null) return null;
        Queue<UndirectedGraphNode> q = new LinkedList<>();
        q.add(node);

        //return start node
        UndirectedGraphNode res = new UndirectedGraphNode(node.label);
        map.put(node, res);

        while(q.size() > 0){
            UndirectedGraphNode tmp = q.poll();
            for(UndirectedGraphNode nei : tmp.neighbors){
                if(!map.containsKey(nei)){
                    map.put(nei, new UndirectedGraphNode(nei.label));
                    q.add(nei);
                }
                map.get(tmp).neighbors.add(map.get(nei));    //not add(nei)!!
            }
        }

        return res;
    }
}
class UndirectedGraphNode {
    int label;
    List<UndirectedGraphNode> neighbors;
    UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
};
