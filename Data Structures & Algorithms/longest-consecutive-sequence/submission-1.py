class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=0: return 0
        return self.calculate_count(set(nums))

    def calculate_count(self, normalized:set):
        count=1
        for i in normalized:
            if i+1 in normalized:
                count+=1
        return count