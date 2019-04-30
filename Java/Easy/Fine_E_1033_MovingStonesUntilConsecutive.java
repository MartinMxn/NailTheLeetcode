class Solution {
    public int[] numMovesStones(int a, int b, int c) {
        //sort by position
        int x = Math.min(a, Math.min(b, c));
        int z = Math.max(a, Math.max(b, c));
        int y = a + b + c - x - z;
        
        //if x previous 2 than z, we can't move
        if (x + 2 == z) return new int[]{0, 0};
        
        //if x-y or y-z have 2 distance, min move is 1
        if (y - x <= 2 || z - y <= 2) return new int[]{1, z - x - 2};
        
        return new int[]{2, z - x - 2};
    }
}
