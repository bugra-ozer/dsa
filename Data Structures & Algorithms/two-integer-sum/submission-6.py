class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            candidate=target-nums[idx]
            if candidate in nums:
                try:
                    second_number=nums.index(candidate, idx+1)
                    return [idx, second_number]
                except ValueError: pass