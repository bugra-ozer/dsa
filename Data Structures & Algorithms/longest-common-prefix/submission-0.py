class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
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
                right+=1
                if right==len(strs):
                    return longest_prefix
            else:
                longest_prefix=deque_prefix.pop()
        return ""