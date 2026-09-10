
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left] == s[right]:
                return False
            right -= 1
            left += 1
            print(f'Iteration: {right}/n{left}')
        return True