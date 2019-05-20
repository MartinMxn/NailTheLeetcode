/**
 * @param {number[]} stones
 * @return {number}
 1.sort the array
 2.pick two if array size > 2
 3.smash and calculate and put into array if not equal
 4.return last one or 0
 */
var lastStoneWeight = function(stones) {
    if (stones.length === 0) return 0;  //! last two may have same weight 
    if (stones.length === 1) return stones[0];
    
    stones.sort((a,b) => a - b);
    let n = stones.length;  
    let dif = Math.abs(stones[n - 1] - stones[n - 2]);
    console.log(stones);
    stones.splice(n - 2, 2);
    if (dif !== 0) stones.push(dif);
    return lastStoneWeight(stones);
};
