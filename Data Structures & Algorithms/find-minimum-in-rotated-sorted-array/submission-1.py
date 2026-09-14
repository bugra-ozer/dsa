class Solution:
    def findMin(self, nums: List[int]) -> int:
        unsorted=nums
        while unsorted!=sorted(unsorted):
            unsorted=self.return_unsorted(unsorted)
        return unsorted[0]
        
    def return_unsorted(self, nums):
        """Returns unsorted nums in rotated sorted array. If there is no unsorted left, returns minimum half"""
        mid=len(nums)//2
        left, right=nums[:mid], nums[mid:]
        if left == sorted(left):
            return right
        elif right == sorted(right):
            return left
        elif right<left:
            return right
        else: return left