class Solution:
    def search(self, nums: List[int], target: int) -> int:
       midpoint=self.getmidpoint(nums)
       if len(nums)<=1: return -1
       if nums[midpoint]==target:return midpoint
       elif nums[midpoint]<target:return self.search(nums[:midpoint],target)
       elif nums[midpoint]>target:return self.search(nums[midpoint:], target)

    def getmidpoint(self, nums:list):
        left=0
        right=len(nums)
        midpoint=(left+right)//2
        return midpoint