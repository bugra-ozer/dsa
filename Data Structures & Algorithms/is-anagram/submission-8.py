class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left=0
        right=len(s)-1
        for i in range(len(s)):
            if not s[left]==s[right]:
                return False
        return True