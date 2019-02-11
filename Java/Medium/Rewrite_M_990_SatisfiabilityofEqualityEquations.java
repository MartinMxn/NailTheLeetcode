class Rewrite_M_990_SatisfiabilityofEqualityEquations {
    int[] union = new int[26];
    public boolean equationsPossible(String[] equations) {
        for(int i = 0; i < 26; i++) union[i] = i;
        //union[find(a)] = find(b)
        for(String eq : equations) {
            if(eq.charAt(1) == '=') 
                union[find(eq.charAt(0) - 'a')] = find(eq.charAt(3) - 'a');
        }
        //find(a) == find(b)
        for(String eq : equations) {
            if(eq.charAt(1) == '!' && find(eq.charAt(0) - 'a') == find(eq.charAt(3) - 'a')) 
                return false;
        }
        
        return true;
    }
    
    private int find(int x){
        if(union[x] != x) union[x] = find(union[x]);
        return union[x];
    }
}
