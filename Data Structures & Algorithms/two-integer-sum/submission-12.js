class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) 
    {
        const dictionary=new Map()
        for (let i = 0; i<nums.length; i++)
        {
            dictionary.set(nums[i], i)
        }

        for (let i =0; i<nums.length; i++)
        {
            const candidate = target - nums[i]
            if (dictionary.has(candidate) && dictionary.get(candidate)!==i)
            {
                return [i, dictionary.get(candidate)]
            }
        }
    }

}   
