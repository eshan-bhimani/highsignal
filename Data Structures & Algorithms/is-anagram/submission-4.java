class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        Hashtable<Character, Integer> sTable = new Hashtable<>();
        Hashtable<Character, Integer> tTable = new Hashtable<>();
        
        for (int i = 0; i < s.length(); i++){
            int frequencyS = 1;
            
            char sChar = s.charAt(i);
            if (sTable.containsKey(sChar)){
                frequencyS++;
            } else{
                sTable.put(sChar, frequencyS);
            }
        }

        for (int j = 0; j < t.length(); j++){
            int frequencyT = 1;
            char tChar = t.charAt(j);
            if (tTable.containsKey(tChar)){
                frequencyT++;
            } else{
                tTable.put(tChar, frequencyT);
            }
        }

        if (sTable.equals(tTable) && tTable.equals(sTable)){
            return true;
        }
        return false;
    }
}
