class Fine_M_991_BrokenCalculator {
    public int brokenCalc(int X, int Y) {
        if(X >= Y) return X - Y;
        int res = 0;
        //if Y is odd, Y could only Y + 1
        //so Change Y to X is only one choice
        while(Y > X) {
            Y = Y % 2 == 0 ? Y / 2 : Y + 1; 
            res++;
        }
        return res + X - Y;
    }
}
