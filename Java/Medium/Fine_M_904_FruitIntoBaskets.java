/*sliding window+ hashmap
store the window we have meet
first part and second, if size of hashmap larger than 2
remove the min position in map.values()
*/
class Solution {
    public int totalFruit(int[] tree) {
        if(tree == null || tree.length == 0) {
            return 0;
        }
        
        int max = 1;
        HashMap<Integer, Integer> valueToPositionMap = new HashMap<>();
        int i = 0, j = 0;
        while(j < tree.length) {
            // if(valueToPositionMap.size() <= 2) {
                valueToPositionMap.put(tree[j], j++);
            // }
            
            //remove the first part pointer
            if(valueToPositionMap.size() > 2) {
                int min = tree.length - 1;
                for(int value : valueToPositionMap.values()) {
                    min = Math.min(min, value);
                }
                i = min + 1;
                valueToPositionMap.remove(tree[min]);
            }
            
            max = Math.max(max, j - i);
        }
        
        return max;
    }
}
/*
O(n)
O(1)
*/
