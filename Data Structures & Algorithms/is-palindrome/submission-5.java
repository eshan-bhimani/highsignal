class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            char cLeft = s.charAt(left);
            char cRight = s.charAt(right);

            // skip non-alphanumeric on the left
            if (!Character.isLetterOrDigit(cLeft)) {
                left++;
                continue;
            }

            // skip non-alphanumeric on the right
            if (!Character.isLetterOrDigit(cRight)) {
                right--;
                continue;
            }

            // compare (case-insensitive)
            if (Character.toLowerCase(cLeft) != Character.toLowerCase(cRight)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
