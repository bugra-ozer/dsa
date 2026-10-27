class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num_index in range(len(numbers)):
            popped_numbers=numbers.copy()
            popped_numbers.pop(num_index)
            num=numbers[num_index]
            candidate=target-num
            if candidate in popped_numbers:
                return [num_index+1, numbers.index(candidate, num_index+1)+1]