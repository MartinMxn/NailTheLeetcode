package Java.Medium;

import java.util.ArrayList;
import java.util.List;

public class OK_M_230_KthSmallestElementinaBST {
    //max heap
//     public int kthSmallest(TreeNode root, int k) {
//         PriorityQueue<Integer> pq = new PriorityQueue<>(k, (a,b) -> b - a);
//         helper(root, k, pq);
//         return pq.poll();
//     }

//     private void helper(TreeNode root, int k, PriorityQueue<Integer> pq) {
//         if(root == null) return;
//         pq.add(root.val);
//         if(pq.size() > k){
//             pq.poll();
//         }
//         if(root.left != null) helper(root.left, k, pq);
//         if(root.right != null) helper(root.right, k, pq);
//     }
    //

    //Without follow up
    //put each node's val into a List and return list.get(k - 1)
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> list = new ArrayList<>();
        inorder(root, k, list);
        return list.get(k - 1);
    }

    private void inorder(TreeNode root, int k, List<Integer> list) {
        if(root == null) return;
        inorder(root.left, k, list);
        list.add(root.val);
        if(list.size() == k) return;
        inorder(root.right, k , list);
    }


    //follow up
    //What if the BST is modified (insert/delete operations) often
    //and you need to find the kth smallest frequently?
    //How would you optimize the kthSmallest routine?

    //count left, then right
    //if count == k, return value
    //else return
    // int res, count;
    // public int kthSmallest(TreeNode root, int k) {
    //     if(root != null){
    //         kthSmallest(root.left, k);
    //         count++;
    //         if(count == k){
    //             res = root.val;
    //             return res;
    //         }
    //         kthSmallest(root.right, k);
    //     }
    //     return res;
    // }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}