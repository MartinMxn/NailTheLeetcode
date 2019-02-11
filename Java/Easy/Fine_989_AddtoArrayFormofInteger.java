class Rewrite_989_AddtoArrayFormofInteger {
    public List<Integer> addToArrayForm(int[] A, int K) {
        List<Integer> list = new ArrayList<>();
        for(int i = A.length - 1; i >= 0; i--) {
            list.add(0, (A[i] + K) % 10 );
            K = (A[i] + K) / 10;
        }
        //take care if K larget than A
        //23
        //K % 10
        //2 -> list
        //K % 10
        //3 -> list
        while(K > 0) {
            list.add(0, K % 10);
            K /= 10;
        }
        return list;
    }
}
