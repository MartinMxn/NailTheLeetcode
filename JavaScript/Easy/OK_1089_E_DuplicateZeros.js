var duplicateZeros = function(arr) {
    len = arr.length
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == 0) {
            arr.splice(i, 0, 0);
            i++
        }
    }
    if (arr.length != len){
        arr.splice(-(arr.length - len))
    }
};
