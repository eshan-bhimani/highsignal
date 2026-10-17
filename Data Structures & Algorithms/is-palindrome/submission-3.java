class Solution {
    public boolean isPalindrome(String s) {

        Stack<Character> stk = new Stack<>();
        Queue<Character> qu = new LinkedList<>();

        for (int i = 0; i < s.length(); i++){
            stk.push(s.charAt(i));
            qu.add(s.charAt(i));
        }

        for (int i = 0; i < s.length(); i++){
            Character fromStack = stk.pop();
            Character fromQueue = qu.remove();
            if (fromStack != fromQueue){
                return false;
            }
        }
        return true;

    }
}
