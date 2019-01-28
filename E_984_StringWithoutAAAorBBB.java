class E_984_StringWithoutAAAorBBB {
    public static String strWithout3a3b(int A, int B) {
        StringBuilder sb = new StringBuilder();
        int lena = 0, lenb = 0;
        int size = A + B;
        for (int i = 0; i < size; i++) {
            if ( (A >= B && lena < 2) || lenb == 2) {
                sb.append("a");
                A--;
                lena++;
                lenb = 0;
            } else {
                sb.append("b");
                B--;
                lenb++;
                lena = 0;
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(strWithout3a3b(1,2 ));
    }
}