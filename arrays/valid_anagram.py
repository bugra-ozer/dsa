from collections import Counter

def isAnagram(s: str, t: str) -> bool:
        chars_first, chars_second = Counter(s), Counter(t)
        if chars_first == chars_second:
            return True
        else: return False

isAnagram("abc", "abc")