class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return merge_sort(nums)

def merge_sort(nums):
    if len(nums)<=1: return nums
    left, right, midpoint = fixture_sub_lists(nums)
    left=merge_sort(left)
    right=merge_sort(right)
    return merge_sides(left, right)

def fixture_sub_lists(nums):
    midpoint = len(nums) // 2
    left = nums[:midpoint]
    right = nums[midpoint:]
    return left, right, midpoint

def merge_sides(left, right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i<len(left):
        for item in left[i:]:
            result.append(item)
    if j<len(right):
        for item in right[j:]:
            result.append(item)
    return result