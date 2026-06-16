class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++){
            char sChar = s.charAt(i);
            int frequencyS = sMap.getOrDefault(sChar, 0) + 1;
            sMap.put(sChar, frequencyS);
        }

        for (int j = 0; j < t.length(); j++){
            char tChar = t.charAt(j);
            int frequencyT = tMap.getOrDefault(tChar, 0) + 1;
            tMap.put(tChar, frequencyT);
        }

        if (sMap.equals(tMap) && tMap.equals(sMap)){
            return true;
        }
        return false;
    }
}
