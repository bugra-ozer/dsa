class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for idx in range(len(nums)):
            candidate = target - nums[idx]
            if candidate in dictionary and dictionary[candidate]!=idx:
                return [dictionary[candidate], idx]
            dictionary[nums[idx]] = idx