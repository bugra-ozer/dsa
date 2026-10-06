class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) 
    {
        const set_nums=new Set(nums)

        return (set_nums.size<nums.length)
    }
}
