class Solution {
    public boolean isPalindrome(String s) {
        String fixed=s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        int left=0;
        int right=fixed.length()-1;
        while (left<right){
            if (fixed.charAt(left) != fixed.charAt(right)){
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}