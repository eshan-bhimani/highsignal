class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int read = nums[i];
            int diff = target - read;
            if (seen.containsKey(diff)){
                return new int[] {seen.get(diff), i};
            }
            seen.put(read, i);
        }

        return new int[] {};

        
        
    }
}
