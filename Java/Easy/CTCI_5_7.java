/*
swap odd and even bits in integer
10 01 11 01
01 10 11 10
*/
class CTCI_5_7 {
    //mask the odd number by 0xaaaaaaaa(101010..) and move left
    //mask the even number by 0x55...(01010101) and move right
    //merge two result
    public int swapOddAndEvenBit(int x) {
        return ( ((x & 0xaaaaaaaa) >>> 1) | ( (x & 0x55555555) << 1) );
    }
}
