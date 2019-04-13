/*
get in O(1) -> hashtable
put in O(1) -> list
remove and move to front in O(1) -> Double Linkedlist

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

*/
class LRUCache {
    private class Node{
        int key;
        int value;
        LRUCache.Node prev;
        LRUCache.Node next;
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
        Node() {
            this.key = 0;
            this.value = 0;
        }
    }
    private HashMap<Integer, LRUCache.Node> map;
    private int capacity;
    private int currentCount;
    private LRUCache.Node head;
    private LRUCache.Node tail;
    
    public LRUCache(int capacity) {
        map = new HashMap<>();
        this.capacity = capacity;
        currentCount = 0;
        head = new LRUCache.Node();
        tail = new LRUCache.Node();
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        LRUCache.Node node = map.get(key);
        if (node == null) {
            return -1;
        } else {
            //update list(remove and moveToFront)
            remove(node);
            addToListFront(node);
            return node.value;
        }
    }
    
    public void put(int key, int value) {
        LRUCache.Node node = map.get(key);
        if (node == null) {
            node = new LRUCache.Node(key, value);
            map.put(key, node);
            addToListFront(node);
            currentCount++;
            
            if (currentCount > capacity) {
                //!!Get removed one first
                LRUCache.Node toDelete = tail.prev;
                //remove from list
                remove(toDelete);
                //remove from map
                map.remove(toDelete.key);
                currentCount--;
            }
        } else {
            // remove the exist node in list and move to front
            remove(node);
            // update map
            node.value = value;
            // update list
            addToListFront(node);
        }
        
    }
    
    private void addToListFront(LRUCache.Node node) {
        LRUCache.Node headNext = head.next;
        headNext.prev = node;
        node.next = headNext;
        head.next = node;
        node.prev = head;
    }
    
    private void remove(LRUCache.Node node) {
        LRUCache.Node prev = node.prev;
        LRUCache.Node next = node.next;
        prev.next = next;
        next.prev = prev;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
