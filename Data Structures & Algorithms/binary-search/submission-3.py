class Solution:
    def search(self, nums: List[int], target: int, left=0, right=None) -> int:
       if not right: right=len(nums)
       midpoint=self.getmidpoint(nums, left, right)
       if left>=right: return -1
       if nums[midpoint]==target:return midpoint
       elif nums[midpoint]<target:
        left=midpoint+1
        return self.search(nums, target, left, right)
       elif nums[midpoint]>target:
        right=midpoint-1
        return self.search(nums, target, left, right)

    def getmidpoint(self, nums:list, left, right):
        midpoint=(left+right)//2
        return midpoint