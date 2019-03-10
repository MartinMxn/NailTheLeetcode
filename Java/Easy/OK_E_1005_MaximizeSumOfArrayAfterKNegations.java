/*
1.
if k is odd, find the smallest one to negate
if k is even, if there is negative one, do the nege and K - 1
                else return the result
2.priorityQueue
*/
class Solution {  
//  1.O(n^2)
//     public int largestSumAfterKNegations(int[] A, int K) {
//         int sum = 0;
//         if(K == 0) {
//             return sumUp(A);
//         }
        
//         //find the smallest one
//         int smallest = findSmallest(A);
//         if(A[smallest] < 0 || K > 0) {
//             A[smallest] = -A[smallest];
//             return largestSumAfterKNegations(A, K - 1);
//         } 
//         return sumUp(A);
//     }
    
//     private int findSmallest(int[] A) {
//         int smallest = A.length - 1;
//         for(int i = 0; i < A.length; i++) {
//             if(A[i] < A[smallest]) {
//                 smallest = i;
//             }
//         }
//         return smallest;
//     }
    
//     private int sumUp(int[] A) {
//         int sum = 0;
//         for(int i = 0; i < A.length; i++) {
//             sum += A[i];
//         }
//         return sum;
//     }
    
}
