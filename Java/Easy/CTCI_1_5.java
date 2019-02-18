/*
check whether two string could edit one char to be same as another one
*/
class Solution {
    public boolean isP(String s, String t) {
        if(s.length() == t.length()){
            return checkReplace(s, t);
        }else if(s.length() == t.length() + 1) {
            return checkOneAddStep(s, t);
        }else if(s.length() + 1 == t.length()) {
            return checkOneAddStep(t, s);
        }
        return false;
    }

    private boolean checkReplace(String s, String t) {
        boolean flag = false;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) != t.charAt(i)) {
                if(flag) return false;
                flag = true;
            }
        }
        return true;
    }

    private boolean checkOneAddStep(String s, String t) {
        //two pointers
        //s is longer
        int p1 = 0, p2 = 0;
        while(p1 < s.length() && p2 < t.length()) {
            if(s.charAt(p1) != t.charAt(p2)) {
                if(p1 != p2) return false;
                p1++;
            } else {
                p1++;
                p2++;
            }
        }
        return true;
    }
}
