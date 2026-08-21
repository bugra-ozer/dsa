class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=''.join(filter(str.isalnum, s.lower()))
        if result[::-1]==result:
            return True
        return False