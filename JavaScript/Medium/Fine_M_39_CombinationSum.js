/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const res = [];
    const helper = (candidates, target, index = 0, tmp=[]) => {
        if(target === 0) {
            res.push(tmp);
        }else{
            for(let i = index; i < candidates.length; i++) {
                if(target - candidates[i] >= 0) {
                    helper(candidates, target - candidates[i], i, tmp.concat(candidates[i]));
                }
            }
        }
        return;
    }
    helper(candidates, target);
    return res;
};
