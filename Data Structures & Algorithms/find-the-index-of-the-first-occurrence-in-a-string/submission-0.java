class Solution {
    public int strStr(String haystack, String needle) {

        for (int i = 0; i <= haystack.length() - needle.length(); i++){
            String find = haystack.substring(i, i + needle.length());
            if (find.equals(needle)){
                return i;
            }
        }
        return -1;
        
    }
}