class OK_E_66_Plus One {
    public int[] plusOne(int[] digits) {
        
//         boolean allNine = true;
//         for(int i : digits){
//             if(i != 9) {
//                 allNine = !allNine;
//                 break;
//             }
//         }
        
//         if(allNine){
//             int[] res = new int[digits.length + 1];
//             Arrays.fill(res, 0);
//             res[0] = 1;
//             return res;
//         }else{
//             int point = digits.length - 1;
//             while(point >= 0){
//                 if(digits[point] < 9){
//                     digits[point]++;
//                     break;
//                 }
//                 digits[point] = 0;
//                 point--;
//             }
//         }
//         return digits;
        
        int len = digits.length;
        for(int i = len - 1; i >= 0; i--){
            if(digits[i] < 9){
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] res = new int[len + 1];
        res[0] = 1;
        return res;
    }
}
