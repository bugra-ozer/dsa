from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_first, chars_second = Counter(s), Counter(t)
        if chars_first == chars_second:
            return True
        else: return False