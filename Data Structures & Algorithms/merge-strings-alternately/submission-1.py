class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        right=0
        result=''
        while right < len(word1) or right<len(word2):
            if left < len(word1) and left < len(word2):
                str_concat=word1[left]+word2[left]
                result+=str_concat
                left+=1
            elif left<len(word1):
                result+=word1[left:]
                return result
            elif left<len(word2):
                x=word2[left:]
                result+=word2[left:]
                return result
            right+=1
        return result