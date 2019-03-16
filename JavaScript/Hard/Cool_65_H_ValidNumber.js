/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    var regex = /^[+-]?((\d+\.?\d*)|(\.\d+))(e[+-]?\d+)?$/
    
    /*
        rules in regExp need to remember:
        ^ start    $ end  
        ? zero or one previous character or expression()
        + one or more ...
        * zero or more ...
        \d any digit
        [abc]? one a or b or c
        \.   .
        |    or
    */
    
    //start with + or -      ^[+-]?
    //two situation, one or more digits before . or not
    //it may looks like 2.3e3 or .3e3
    
    //if one or more digits
    //one or more digits \d+ and zero or one . \.? and any digits after \d*
    //if not digit
    //at least one digit after .      \.\d+ 
    //relation is 'or', so conncet with |,  ^[+-]?((\d+\.?\d*)|(\.\d+))
    
    //then deal with e and digits after e
    //e[+-]?  -> e with + or -
    //\d+ with at least one digit
    //$ must at the end
    
    //test return true if there's at least one match
    return regex.test(s.trim());
};
