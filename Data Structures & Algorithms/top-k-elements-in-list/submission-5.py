class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq=Counter(nums)
        result=[]
        for val, freq in nums_freq.most_common(k):
            result.append(val)
        return result