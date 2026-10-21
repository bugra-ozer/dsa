class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;

        while(left<=right){
            int midpoint = (left+right)/2;
            int value = nums[midpoint];
            if (value==target){
                return midpoint;
            }
            else if(value<target){
                left=midpoint+1;
            }
            else if(value>target){
                right=midpoint-1;
            }
        }
        return -1;
    }
}
