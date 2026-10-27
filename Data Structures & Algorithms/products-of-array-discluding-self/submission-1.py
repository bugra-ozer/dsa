from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for num in range(len(nums)):
            left_side=nums[:num]
            right_side=nums[num+1:]
            merged=left_side+right_side
            result.append(reduce(lambda x,y: x*y, merged))
        return result