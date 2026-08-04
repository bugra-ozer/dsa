from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]):
        result=[]
        dictionary=self.MapStrings(strs)
        for value in dictionary.values():
            result.append(value)
        return result

    def MapStrings(self, strs: list[str]):
        """Given list of strings, separates strings in dictionary to their sorted chars as keys."""
        dictionary = {}
        for str in strs:
            dictionary.setdefault(''.join(sorted(str)), [])
            dictionary[''.join(sorted(str))].append(str)
        return dictionary