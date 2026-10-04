class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        minimal=set(nums)
        if len(nums)==len(minimal):
            return False
        else: return True