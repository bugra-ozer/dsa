from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        for num in range(len(nums)):
            copy=nums.copy()
            copy.pop(num)
            result.append(reduce(lambda x,y: x*y, copy))
        return result