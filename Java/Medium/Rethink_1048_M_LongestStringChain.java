/*
1.sort based on length
2.loop from first one and update map based on prev string value (delete one char) in the map
*/
class Solution {
 
    public int longestStrChain(String[] words) {
        if (words == null || words.length == 0) return 0;
        
        Arrays.sort(words, new Comparator<String>(){
            public int compare(String str1, String str2) {
                return str1.length() - str2.length();
            }
        });
        
        int res = 0;
        HashMap<String, Integer> map = new HashMap();
        
        for (String word : words) {
            if (map.containsKey(word)) continue;
            map.put(word, 1);
            
            for (int i = 0; i < word.length(); i++) {
                StringBuilder sb = new StringBuilder(word);
                sb.deleteCharAt(i);
                String prev = sb.toString();
                if (map.containsKey(prev) && map.get(prev) + 1 > map.get(word)) {
                    map.put(word, map.get(prev) + 1);
                }
            }
            
            res = Math.max(res, map.get(word));
        }
        
        return res;
    }
}
