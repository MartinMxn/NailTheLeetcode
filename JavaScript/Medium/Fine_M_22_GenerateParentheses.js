/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    if(n === 0) return [];
    var res = [];
    helper(n, n, "", res);
    return res;
};

function helper(open, close, curStr, res) {
    if(open === 0 && close === 0) {
        res.push(curStr);
        return;
    }
    if(close < open) return;
    if(open >= 1) helper(open - 1, close, curStr + "(", res);
    if(close >= 1) helper(open, close - 1, curStr + ")", res);
    
    return;
}
