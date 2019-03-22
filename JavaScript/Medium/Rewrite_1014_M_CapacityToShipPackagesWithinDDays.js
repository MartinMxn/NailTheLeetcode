/**
 * @param {number[]} weights
 * @param {number} D
 * @return {number}
 
 reverse think
 take a guess and binary search from RESULT!!
 */
var shipWithinDays = function(weights, D) {
    let left = 0, right = 0;
    for(let i of weights) {
        left = Math.max(i, left);
        right += i;
    }
    
    while(left < right) {
        let mid = (right + left) / 2;
        let cur = 0, need = 1;
        for(let i of weights) {
            if(cur + i > mid) {
                need++;
                cur = 0;
            }
            cur += i;
        }
        if(need > D) left = mid + 1;
        else right = mid;
    }
    return left - 1;
};
