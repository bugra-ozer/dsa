class Solution:
    def searchInsert(self, nums: List[int], target: int, left=0 ,right=None) -> int:
        if right is None: right=len(nums)-1

        if left > right:
            print(left, right)
            if left-right<2:
                return left

        midpoint=(left+right)//2

        if nums[midpoint]==target:
            return midpoint
        elif nums[midpoint]<target:
            left=midpoint+1
            return self.searchInsert(nums, target, left, right)
        elif nums[midpoint]>target:
            right=midpoint-1
            return self.searchInsert(nums, target, left, right)