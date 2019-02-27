/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val,List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
    public Node cloneGraph(Node node) {
        if(node == null) return null;
        Node res = new Node(node.val, new LinkedList<Node>());
        HashMap<Node, Node> map = new HashMap<>();
        Queue<Node> q = new LinkedList<>();
        map.put(node, res);
        q.offer(node);
        while(!q.isEmpty()) {
            Node tmp = q.poll();
            for(Node nei : tmp.neighbors) {
                if(!map.containsKey(nei)) {
                    map.put(nei, new Node(nei.val, new LinkedList<Node>()));
                    q.add(nei);
                }
                map.get(nei).neighbors.add(map.get(tmp));
            }
            
        }
        return res;
    }
}
