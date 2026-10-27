

class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        if not self.isPalindrome(s):#not palindrome
            return self.checkPalindromeDrop(s)
        elif self.isPalindrome(s) and len(s)%2==0: #already palindrome and even length
            return False
        elif self.isPalindrome(s) and len(s)%2!=0: #already palindrome and odd length
            return self.checkPalindromeDrop(s)

    def checkPalindromeDrop(self, s):
        for i in range(len(s)):
            substring=s[:i-1]+s[i:]
            if self.isPalindrome(substring):
                return True
        return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left] == s[right]:
                return False
            right -= 1
            left += 1
            print(f'Iteration: {right}/n{left}')
        return True