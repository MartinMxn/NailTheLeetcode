package Java.Medium;

public class WTF_M_880_DecodedStringatIndex {
//   public String decodeAtIndex(String S, int K) {
//         //Memory exceed, don't need to get all string
//         if(K == 1) return S.substring(0, 1);
//         String st = "";

//         for(char c : S.toCharArray()) {
//             System.out.println(st);
//             if(st.length() >= K) return st.charAt(K - 1) + "";
//             if(!Character.isDigit(c)){
//                 st += c + "";
//             }else{
//                 System.out.println(c);
//                 System.out.println(st);
//                 String tmp = st;
//                 for(int i = 1; i < c - '0'; i++){
//                     st += tmp;
//                 }
//                 System.out.println(st);
//             }
//         }
//         return st.charAt(K - 1) + "";   //the last char is digit
//     }

    public String decodeAtIndex(String S, int K) {
        long size = 0;
        int N = S.length();

        // Find size = length of decoded string
        for (int i = 0; i < N; ++i) {
            char c = S.charAt(i);
            if (Character.isDigit(c))
                size *= c - '0';
            else
                size++;
        }
        System.out.println(size);

        for (int i = N-1; i >= 0; --i) {
            char c = S.charAt(i);
            K %= size;
            if (K == 0 && Character.isLetter(c))
                return Character.toString(c);

            if (Character.isDigit(c))
                size /= c - '0';
            else
                size--;
        }

        throw null;
    }
}
