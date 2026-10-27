from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=return_buckets(nums)
        winners=[]
        visited_keys=[]
        winners, visited_keys=populate_winners(winners, bucket, k, visited_keys)
        return winners

def return_buckets(nums_list:list):
    nums=Counter(nums_list)
    bucket={}
    for k, v in nums.items():
        bucket.setdefault(v, [])
        bucket[v].append(k)
    return bucket

def populate_winners(winners:list, bucket:dict, k:int, visited_keys:list):
    while len(winners)<k:
        max_key, visited_keys = unused_max_key(visited_keys, bucket)
        if len(bucket[max_key])<=k and winners == []:
            winners=bucket[max_key]
        elif len(winners)<k:
            for item in bucket[max_key]:
                if len(winners)<k:
                    winners.append(item)
    return winners, visited_keys

def unused_max_key(visited_keys:list, bucket:dict):
    """Return the unused and bucket populated key"""
    max_key = max(bucket.keys())
    while max_key in visited_keys or len(bucket[max_key])==0:
        max_key = max(bucket.keys())-1
    visited_keys.append(max_key)
    return max_key, visited_keys