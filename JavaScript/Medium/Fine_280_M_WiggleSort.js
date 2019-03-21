var wiggleSort = function(nums) {
    nums.sort((a, b) => {
        return a - b;
    });
    
    for(let i = 1; i < nums.length; i+=2) {
        if(i + 1 < nums.length)
            [nums[i], nums[i + 1]] = [nums[i + 1], nums[i]];        
    }
};
