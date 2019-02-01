package Java.Easy;

public class OK_E_844_BackspaceStringCompare {
    public boolean backspaceCompare(String S, String T) {
        StringBuilder s = new StringBuilder();
        StringBuilder t = new StringBuilder();

        for(char c : S.toCharArray()) {
            if(c == '#'){
                if(s.length() > 0) s.deleteCharAt(s.length() - 1);
            }else{
                s.append(c);
            }
        }

        for(char c : T.toCharArray()) {
            if(c == '#'){
                if(t.length() > 0) t.deleteCharAt(t.length() - 1);
            }else{
                t.append(c);
            }
        }

        return s.toString().equals(t.toString());
    }
}
