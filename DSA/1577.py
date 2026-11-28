from collections import Counter

class Solution:

    # Square num logic:
    # Say the item on nums1 is 7. 7^2 is 49.
    # Check what are the things that can make 49?
    # We check if current idx from nums2 divide with 49 without remainder.
    # It does, we have a target (which is another 7 for 49)
    # Then grow hashmap regardless of numbers,
    # If got the target in hashmap, grow the res (which is local)
    # And finally return

    # For nums1=[1,1] nums2=[1,1,1] pair, nums1[0]->1 for that one 0,1 | 0, 2 | 1, 2 is valid. res = 3
    # Next iteration nums1[1]->1 for that one again 0,1 | 0, 2 | 1, 2 is valid. res = 6
    # Now flip it (for type2):
    # nums2=[1,1,1] and nums1=[1,1] nums2[0]->1 for that one 0,1 is valid only. res = 7
    # nums2=[1,1,1] and nums1=[1,1] nums2[1]->1 for that one 0,1 is valid only. res = 8
    # nums2=[1,1,1] and nums1=[1,1] nums2[2]->1 for that one 0,1 is valid only. res = 9
    # done.
    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        freq_one, freq_two=Counter([item**2 for item in nums1]), Counter([item**2 for item in nums2])

        def square_sum(nums, square):
            hash_map = {}
            res=0
            for idx in range(len(nums)):
                if square % nums[idx] == 0:
                    target = square // nums[idx]
                    if target in hash_map:
                        res+=hash_map[target]
                    hash_map.setdefault(nums[idx], 0)
                    hash_map[nums[idx]]+=1
            return res

        result=0
        for square, value in freq_one.items():
            local_result = 0
            local_result+=square_sum(nums2, square)
            local_result=local_result*value
            result+=local_result
        for square, value in freq_two.items():
            local_result = 0
            local_result+=square_sum(nums1, square)
            local_result=local_result*value
            result+=local_result
        return result