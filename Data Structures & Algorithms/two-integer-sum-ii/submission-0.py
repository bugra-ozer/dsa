class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num_index in range(len(numbers)):
            num=numbers[num_index]
            candidate=target-num
            if candidate in numbers:
                return [num_index+1, numbers.index(candidate)+1]