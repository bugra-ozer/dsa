class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result=[]
        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            if index > 0 and nums[index] == nums[index - 1]: continue
            while left<right:
                candidate_nums=[nums[index],nums[left],nums[right]]
                candidate=nums[index]+nums[left]+nums[right]
                if candidate == 0 and candidate_nums not in result:
                    result.append(candidate_nums)
                    left+=1
                    right-=1
                elif candidate == 0:
                    left += 1
                    right -= 1
                elif candidate<0: left+=1
                elif candidate>0: right-=1
        return result