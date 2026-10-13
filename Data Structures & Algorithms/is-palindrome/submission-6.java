class Solution {
    public boolean isPalindrome(String s) {
        String fixed=s;

        int left=0;
        int right=fixed.length()-1;
        while (left<right){
            if (!Character.isLetterOrDigit(fixed.charAt(left))){
                left++;
            }
            else if (!Character.isLetterOrDigit(fixed.charAt(right))){
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