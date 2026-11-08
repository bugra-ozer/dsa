class Solution {
    public boolean isPalindrome(String s) {
        String fixed=s;

        int left=0;
        int right=fixed.length()-1;
        while (left<right){
            if (Character.toString(fixed.charAt(left)).matches("[^a-zA-Z0-9]")){
                left++;
            }
            else if (Character.toString(fixed.charAt(right)).matches("[^a-zA-Z0-9]")){
                right--;
            }

            else {
                if (Character.toLowerCase(fixed.charAt(left)) != Character.toLowerCase(fixed.charAt(right))){
                    return false;
                }
            
                left++;
                right--;
            }
        }

        return true;
    }
}