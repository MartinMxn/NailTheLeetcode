/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    //take care of the type of input here
    //here is a string, so digits.length === 0
    if(digits.length === 0) return [];
    const map = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }
    const res = [];
    const len = digits.length;
    //a - d, a - e
    const dfs = (digits, index = 0, tmp = "") => {
        if(tmp.length === len) { 
            res.push(tmp); 
        }
        else{
            for(let letter of map[digits[index]]) {
                dfs(digits, index + 1, tmp + letter);
            }
        }
        
    }
    
    dfs(digits);
    return res;
};
