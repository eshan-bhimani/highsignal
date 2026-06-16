class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> results = new HashMap<>();

        for (String word : strs){
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sorted = new String(charArray);
            results.putIfAbsent(sorted, new ArrayList<>());
            results.get(sorted).add(word);
        }

        return new ArrayList<>(results.values());
        
    }
}
