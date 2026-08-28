class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """"""
        #req window slides len(s1) at a time so left and right moves together
        left=0
        right=0
        s1_counter=Counter(s1)
        if len(s1)>len(s2): return False
        while right < len(s2):
            if right==0:
                right=len(s1)
                s2_counter=Counter(s2[:len(s1)])
            else:
                left+=1
                right+=1
                s2_counter=Counter(s2[left:right])
            if s1_counter==s2_counter: return True
            if right==len(s2): return False