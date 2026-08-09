class Solution:

    def encode(self, strs: List[str]) -> str:
        result=''
        for string in strs:
            result+=str(len(string))+'prefix='+string
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
        while len(s)>0:
            prefix_index = s.find('prefix=')
            length_string=s[0:prefix_index]
            word_start=len(length_string)+len('prefix=')
            word=s[word_start:int(length_string)+word_start]
            s=s[word_start+len(word):]
            result.append(word)
        return result