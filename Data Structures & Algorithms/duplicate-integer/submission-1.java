class Solution {
    public boolean hasDuplicate(int[] nums) {

        Set<Integer> seen = new HashSet<>();

        for (int i = 0; i < nums.length; i++){
            int read = nums[i];
            if (seen.contains(read)){
                return true;
            }
            seen.add(read);
        }
        return false;
    }
}