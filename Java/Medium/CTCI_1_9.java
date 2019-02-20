/*
* given a function isSubstring
* check if s2 is a rotation of s1
* "waterbottle" is rotation of "erbottlewat"
* */
class CTCI_1_9 {
    /*  s1              s2
    * waterbottle - erbottlewat
    * waterbottlewaterbottle
    * */
    public boolean isRotation(String s1, String s2) {
        //simply look at s1 concatenate with s1
        //if s2 is a substring of it return true
        if(s1.length() == s2.length() && s1.length() > 0) {
            return isSubString(s1 + s1, s2);
        }
        return false;
    }

    private boolean isSubString(String s1, String s2) {
        return s1.contains(s2);
    }
}
