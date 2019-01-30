package Java.Medium;

import java.util.HashMap;
import java.util.TreeMap;

public class Fine_M_981_TimeBased {
    HashMap<String, TreeMap<Integer, String>> map;
    /** Initialize your data structure here. */
    public Fine_M_981_TimeBased() {
        map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        if(!map.containsKey(key)){
            map.put(key, new TreeMap<Integer, String>());
        }
        map.get(key).put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        if(!map.containsKey(key)) return "";
        Integer max = map.get(key).floorKey(timestamp);
        if(max == null) return "";
        else return map.get(key).get(max);
    }
}
