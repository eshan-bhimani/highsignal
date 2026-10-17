class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++){
            int count = 1;
            char sChar = s.charAt(i);
            if(!sMap.containsKey(sChar)){
                sMap.put(sChar, count);
            }
            else if (sMap.containsKey(sChar)){
                count++;
            }
        }

        for (int j = 0; j < t.length(); j++){
            int count = 1;
            char tChar = t.charAt(j);
            if(!tMap.containsKey(tChar)){
                tMap.put(tChar, count);
            }
            else if (tMap.containsKey(tChar)){
                count++;
            }

        }

        if (sMap.equals(tMap) && tMap.equals(sMap)){
            return true;
        }
        return false;
    }
}
