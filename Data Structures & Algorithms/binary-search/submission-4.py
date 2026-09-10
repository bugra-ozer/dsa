class Solution:
    def search(self, nums: List[int], target: int, left=0, right=None) -> int:
        if right is None:
            right = len(nums) - 1

        if left > right:
            return -1

        midpoint = self.getmidpoint(nums, left, right)

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            left = midpoint + 1
            return self.search(nums, target, left, right)
        elif nums[midpoint] > target:
            right = midpoint - 1
            return self.search(nums, target, left, right)

    def getmidpoint(self, nums: list, left, right):
        midpoint = (left + right) // 2
        return midpoint
