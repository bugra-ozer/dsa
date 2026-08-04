class Solution:
    def hasDuplicate(self, nums) -> bool:
        minimal=set(nums)
        if len(nums)==len(minimal):
            return False
        else: return True