/*
* 32-bit number n and m
* insert M to N
* M start at bit j ends at bit i
* */
class CTCI_5_1 {
    /*
    * 1. clear the bit from i to j in n
    * 2. shift m i bit
    * 3. AND two number
    * */
    public int insertion(int n, int m, int i, int j) {
       //1
        //11010101
        //   ^ ^
        //11100011
        //get all one
        //clear left & right
        //get mask
        int allOne = ~0;
        int left = allOne << (j + 1);
        int right = (1 << i) - 1;
        int mask = left | right;
        
        int nAfterClear = n & mask;
        int mAfterShift = m << i;
        //combine them by OR
        return nAfterClear | mAfterShift;
    }
}
