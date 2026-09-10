import string

class Solution:
    def isValid(self, s: str) -> bool:
        key_deque=deque()
        dictionary= {'(': ')', '[': ']', '{': '}'}
        dictionary_reverse={')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in dictionary.keys(): #char is a openning key
                key_deque.append(char)
            elif char in dictionary.values():
                if key_deque:
                    required_key=key_deque.pop()
                    if not dictionary_reverse[char]==required_key:
                        return False
                    else: continue
                return False
        if key_deque: return False
        return True