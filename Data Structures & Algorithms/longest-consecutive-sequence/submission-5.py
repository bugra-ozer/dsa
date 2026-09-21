class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        result = 0
        for i in set_nums:
            if i - 1 not in set_nums:
                count = 1
                candidate=i
                while candidate+1 in set_nums:
                    count+=1
                    candidate+=1

                if count>result: result=count
        return result