class OK_E_509_FibonacciNumber {
//     int[] cache = new int[31];
//     public int fib(int N) {
//         int res = 0;
//         for(int i = 1; i <= N; i++) {
//             if(cache[N] != 0) {
//                 return cache[N];
//             }
//             if(N < 2) {
//                 res = N;
//             } else {
//                 cache[N] = fib(N - 1) + fib(N - 2);
//             }
//         }
//         return res;
//     }
    public int fib(int N) {
        if(N == 0 || N == 1) return N;
        int[] cache = new int[N + 1];
        cache[0] = 0;
        cache[1] = 1;
        for(int i = 2; i <= N; i++) {
            cache[i] = cache[i - 1] + cache[i - 2];
        }
        return cache[N];
    }
}
