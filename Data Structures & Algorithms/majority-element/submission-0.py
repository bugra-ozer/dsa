

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        max_count=0
        for k,v in count.items():
            if v>max_count:
                max_count=v
                max_key=k
        return max_key