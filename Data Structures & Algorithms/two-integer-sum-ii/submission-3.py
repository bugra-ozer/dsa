class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=1
        right=len(numbers)
        while left<right:
            result=numbers[left-1]+numbers[right-1]
            if result < target: left+=1
            elif result > target: right-=1
            elif result == target: return [left, right]