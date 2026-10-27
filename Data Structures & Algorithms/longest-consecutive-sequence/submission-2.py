class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """"""
        return self.calculate_count(set(nums))

    def calculate_count(self, set_nums:set):
        count=1
        result=0
        for i in set_nums:
            while i - 1 in set_nums:
                i=i-1
            while i + 1 in set_nums:
                count +=1
                i+=1
            if count > result:
                result=count
            count=1
        return result