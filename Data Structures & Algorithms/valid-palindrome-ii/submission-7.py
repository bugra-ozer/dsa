

class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        
        left = 0
        right = len(s)-1
        if len(s)==1 or len(s)==2: return True
        while left < right:
            if not s[left] == s[right]:
                if self.isPalindrome(s[left+1:right+1]): #skip left
                    return True
                elif self.isPalindrome(s[left:right]): #skip left
                    return True
                else: return False
            right -= 1
            left += 1
        return True

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left] == s[right]:
                return False
            right -= 1
            left += 1
        return True, left
