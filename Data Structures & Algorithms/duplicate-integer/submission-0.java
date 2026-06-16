class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashMap<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int read = nums[i];
            if (seen.containsKey(read)){
                return true;
            }
            seen.put(read, read);
        }

        return false;
        
    }
}