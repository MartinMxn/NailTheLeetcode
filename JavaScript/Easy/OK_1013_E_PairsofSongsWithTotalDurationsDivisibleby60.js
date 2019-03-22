/**
 * @param {number[]} time
 * @return {number}
 
 two sum after mod by 60
 */
var numPairsDivisibleBy60 = function(time) {
    let count = 0;
    let map = new Array(60).fill(0);
    for(let i = 0; i < time.length; i++) {
        let tmp = 60 - time[i] % 60;  //deal with 0, make amends to 60
        count += map[tmp % 60];
        map[time[i] % 60]++;
    }
    return count;
};
