class Solution {
    public boolean isPalindrome(String s) {


        int left = 0;
        int right = s.length() -1;

        for (int i = 0; i < s.length(); i++){
            char cLeft = s.charAt(left);
            char cRight = s.charAt(right);

            if (!Character.isLetterOrDigit(cLeft)){
                left++;
                continue;
            }
            if (!Character.isLetterOrDigit(cRight)){
                right--;
                continue;
            }

            if (Character.toLowerCase(cLeft) != Character.toLowerCase(cRight)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
