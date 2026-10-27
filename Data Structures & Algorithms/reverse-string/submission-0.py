class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        result = ''
        for char in s:
            result=result.join(reversed(char))
        return result