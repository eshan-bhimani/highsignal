class Solution {
    public boolean isAnagram(String s, String t) {

        Hashtable<Character, Integer> sTable = new Hashtable<>();
        Hashtable<Character, Integer> tTable = new Hashtable<>();

        for (int i = 0; i < s.length(); i++){
            char sChar = s.charAt(i);
            int frequency = 0;
            sTable.put(sChar, frequency);
        }

        for (int j = 0; j < t.length(); j++){
            char tChar = t.charAt(j);
            int frequency = 0;
            tTable.put(tChar, frequency);
        }

        if (sTable.equals(tTable) && tTable.equals(sTable)){
            return true;
        }
        return false;
    }
}
