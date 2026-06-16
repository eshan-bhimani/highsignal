
class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            int difference = target - num;
            if (seen.containsKey(difference)){
                return new int[] {seen.get(difference), i};
            }
            seen.put(num, i);
        }
        return new int[] {};
    }
}