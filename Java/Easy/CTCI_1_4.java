import java.util.HashMap;

class CTCI_1_4 {
    public boolean isP(String s) {
        String st = s.toLowerCase();
        HashMap<Character, Integer> map = new HashMap<>();
        for(char c : st.toCharArray()) {
            if(c != ' ')
                map.put(c, map.getOrDefault(c, 0) + 1);
        }
        int oddCount = 0;
        for(Integer i : map.values()) {
            if(i % 2 == 1) oddCount++;
        }
        return oddCount <= 1;
    }
}
