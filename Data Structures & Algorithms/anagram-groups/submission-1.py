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
            sorted_str=''.join(sorted(str))
            dictionary.setdefault(sorted_str, [])
            dictionary[sorted_str].append(str)
        return dictionary