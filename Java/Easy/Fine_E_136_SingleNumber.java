class Solution {
    public int singleNumber(int[] nums) {
        //1.hash
//         HashMap<Integer,Integer> map = new HashMap<>();
//         for(int i = 0; i < nums.length; i++){
//             if(!map.containsKey(nums[i])){
//                 map.put(nums[i],1);
//             }else{
//                 map.put(nums[i],map.get(nums[i])+1); //map.get(num[i])
//             }
//         }
        
//         for(Integer key: map.keySet()){
//             if(map.get(key) == 1)
//                 return key;
//         }
        
//         return 0;
        //2.bit with ^
        // ^ make the res to 0 when meet the same number
        // and 0 ^ number = number
        // !! a^b^a = (a^a)^b = b 
        // ^ could be seen as non carry add operation!!
        int res = 0;
        for(int i : nums) {res ^= i; System.out.println(res);}  
        return res;
    }
}
