/**
 * @param {string} S
 * @return {string}
 1.go through char in S
 2.check whether the top of stack is same as current char
    if same, pop stack
    if not, push in
 3.concat the stack to String
 */
var removeDuplicates = function(S) {
    let stack = [];
    for (let i = 0; i < S.length; i++) {
        if (stack.length === 0 || stack[stack.length - 1] !== S[i]) {
            stack.push(S[i]);
        } else {
            stack.pop();
        }
    }
    return stack.join("");
};
