class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++){
            int frequencyS = 1;

            char sChar = s.charAt(i);
            if (sMap.containsKey(sChar)){
                frequencyS++;
            } else{
                sMap.put(sChar, frequencyS);
            }
        }

        for (int j = 0; j < t.length(); j++){
            int frequencyT = 1;
            char tChar = t.charAt(j);
            if (tMap.containsKey(tChar)){
                frequencyT++;
            } else{
                tMap.put(tChar, frequencyT);
            }
        }

        if (sMap.equals(tMap) && tMap.equals(sMap)){
            return true;
        }
        return false;
    }
}
