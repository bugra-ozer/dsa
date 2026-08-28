class Solution:
    def minWindow(self, s: str, t: str) -> str:
        got={}
        need=Counter(t)
        have=0
        left=0
        right=0
        min_length=float('inf')
        min_start_idx=0
        while right < len(s):
            got.setdefault(s[right], 0)
            got[s[right]]+=1
            if s[right] in need:
                if got[s[right]]==need[s[right]]:
                    have+=1
            while have==len(need):
                current_length = right - left + 1
                if current_length < min_length:
                    min_length=current_length
                    min_start_idx=left
                got[s[left]]-=1
                if s[left] in need and got[s[left]] < need[s[left]]: have-=1
                left+=1
            right+=1
        if min_length==float('inf'): return ""
        return s[min_start_idx:min_start_idx+min_length]
