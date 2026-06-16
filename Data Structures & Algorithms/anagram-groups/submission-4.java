class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, List<String>> result = new HashMap();

        for (String word : strs){
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);
            result.putIfAbsent(sortedWord, new ArrayList<>());
            result.get(sortedWord).add(word);
        }
        return new ArrayList<>(result.values());
    }
}
