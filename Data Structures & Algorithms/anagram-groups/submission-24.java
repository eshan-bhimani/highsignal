class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> result = new HashMap<>();

        for (String word : strs){
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sorted = new String(charArray);
            result.putIfAbsent(sorted, new ArrayList<>());
            result.get(sorted).add(word);

        }

        return new ArrayList<>(result.values());
        
    }
}
