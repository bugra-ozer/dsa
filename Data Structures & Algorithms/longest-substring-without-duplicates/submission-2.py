class Solution:
    def lengthOfLongestSubstring(self, s: str):
        """"""
        dictionary={}
        max_count=0
        left=0
        right=0
        while right < len(s):
            if s[right] in dictionary and dictionary[s[right]]>=left:
                left=dictionary[s[right]]+1
            dictionary[s[right]]=right
            right+=1
            if right-left>max_count: max_count=right-left
        return max_count