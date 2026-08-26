class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq=0 #highest char freq in the moment
        max_count=0 #best window
        left=0
        right=0
        dictionary={}
        while right < len(s):
            dictionary[s[right]]=dictionary.setdefault(s[right], 0)+1
            if dictionary[s[right]]>max_freq: max_freq=dictionary[s[right]]
            need_replace=(right-left+1)-max_freq
            if need_replace>k:
                left+=1
                dictionary[s[left-1]]-=1
            right+=1
            if right-left>max_count: max_count=right-left
        return max_count