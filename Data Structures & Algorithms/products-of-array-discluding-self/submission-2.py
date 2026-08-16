from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        left=[1]*len(nums)
        right=[1]*len(nums)
        for index in range(len(nums)-1):
            left[index+1]=left[index]*nums[index]
        for index in range(len(nums)-2, -1,-1):
            right[index]=right[index+1]*nums[index+1]
        for index in range(len(nums)):
            result.append(left[index]*right[index])
        return result