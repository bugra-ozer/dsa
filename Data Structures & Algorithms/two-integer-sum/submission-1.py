class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            candidate=target-nums[idx]
            if candidate in nums:
                second_number=nums.index(candidate)
                return [idx, second_number]