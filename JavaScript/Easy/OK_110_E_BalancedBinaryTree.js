/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
//set flag to check if there is Not a BBT at substree, so no need to check each node's subtree
var isBalanced = function(root) {
    let flag = true;
    let tree = (node) => {
        if(!flag) return;
        if(!node) return 0;
        let left = tree(node.left);
        let right = tree(node.right);
        if(Math.abs(left - right) > 1) {
            flag = false;
            return;
        } 
        return Math.max(left, right) + 1;
    }
    tree(root);
    return flag;
};
