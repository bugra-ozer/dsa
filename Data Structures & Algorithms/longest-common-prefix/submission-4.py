class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1 or strs[0]=='':
            return strs[0]

        deque_prefix=deque()
        max_string=''
        for i in strs[0]:
            prefix=''.join(i)
            max_string+=prefix
            deque_prefix.append(max_string)

        right=1
        longest_prefix=deque_prefix.pop()
        while right < len(strs):
            if longest_prefix in strs[right]:
                if right==len(strs)-1:
                    return longest_prefix
                right += 1
            else:
                if not deque_prefix: return ""
                longest_prefix=deque_prefix.pop()
        return ""