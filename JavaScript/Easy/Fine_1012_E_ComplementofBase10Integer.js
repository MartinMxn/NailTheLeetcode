/**
 * @param {number} N
 * @return {number}
 
 
 toString(2)
 parseInt('')
 */
var bitwiseComplement = function(N) {
    if(N === 0) return 1; 
    let based2 =  N.toString(2);
    let res = '';
    for(let i = 0; i < based2.length; i++) {
        if(based2[i] === '1') res += '0';
        else res+= '1';
    }
    return parseInt(res, 2);    //second parameter is the original parsed string's base
};
