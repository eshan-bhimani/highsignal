class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> res = new HashMap<>();

        for(String word : strs){
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);
            res.putIfAbsent(sortedWord, new ArrayList<>());
            res.get(sortedWord).add(word);
        }
        return new ArrayList<>(res.values());

    }
}
