class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            dictionary = {}
            for idx in range(len(nums)):
                dictionary[nums[idx]] = idx

            for idx in range(len(nums)):
                candidate = target - nums[idx]
                if candidate in dictionary and dictionary[candidate]!=idx:
                    return [idx, dictionary[candidate]]