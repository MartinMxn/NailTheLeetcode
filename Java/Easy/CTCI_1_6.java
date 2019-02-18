class CTCI_1_6 {
    public String compress(String s) {
        StringBuilder sb = new StringBuilder();
        int consecutive = 0;
        for(int i = 0; i < s.length(); i++) {
            consecutive++;
            // ! >=
            if(i + 1 >= s.length() || s.charAt(i) != s.charAt(i + 1)) {
                sb.append(s.charAt(i));
                sb.append(consecutive);
                consecutive = 0;
            }
        }
        return sb.length() < s.length() ? sb.toString() : s;
    }
}
