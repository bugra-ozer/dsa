class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size_s=len(s)-1
        copy_s=s.copy()
        for string in copy_s:
            s[size_s]=string
            size_s-=1
        return s