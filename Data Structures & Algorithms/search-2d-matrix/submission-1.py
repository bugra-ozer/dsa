class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sub_list in matrix:
            if self.isCorrectList(sub_list, target):
                return target in sub_list
        return False
    
    def isCorrectList(self, sub_list, target):
        print(sub_list, target)
        if sub_list[len(sub_list)-1]>=target: 
            return True
        return False
