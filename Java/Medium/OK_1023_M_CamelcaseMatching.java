class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        List<Boolean> res = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        for (char c : pattern.toCharArray()) {
            sb.append("[a-z]*" + c + "[a-z]*");
        }
        String reg = "^" + sb.toString() + "$";
        for (String q : queries) {
            res.add(q.matches(reg));
        }
        return res;
    }
}
