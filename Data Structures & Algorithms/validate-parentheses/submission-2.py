import string

class Solution:
    def isValid(self, s: str) -> bool:
        dictionary={'(': ')', '{':'}', '[':']'}
        items=[]
        for char in s:
            if char in string.ascii_letters:
                pass
            elif char in dictionary.keys():
                items.append(char)
            elif char in dictionary.values():
                if not items: return False
                elif char!=dictionary[items[-1]]:
                    return False
                else:
                    items.pop(-1)
        if not items: return True
        else: return False