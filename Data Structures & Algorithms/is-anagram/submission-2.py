class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False
        chars_first, chars_second = list(s), list(t)
        counter=0
        for char in chars_first:
            if counter == len(chars_first)-1 and char in chars_second:
                return True
            if char in chars_second:
                counter+=1
                chars_second=self.reduce_list(char, chars_second)
            else: return False
            
    @staticmethod
    def reduce_list(char, chars:list):
        char_index=chars.index(char)
        chars.pop(char_index)
        new_chars=chars
        return new_chars