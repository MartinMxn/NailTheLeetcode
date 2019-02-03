/**
 * @param {number} A
 * @param {number} B
 * @return {string}
 */
var strWithout3a3b = function(A, B) {
    var lena = 0, lenb = 0;
    var res = "";
    var size = A + B;
    for(let i = 0; i < size; i++) {
        if(lena < 2 && A >= B || lenb === 2){
            res += "a";
            lenb = 0;
            A--;
            lena++;
        } else {
            res += "b";
            lena = 0;
            B--;
            lenb++;
        }
    }
    return res;
};
