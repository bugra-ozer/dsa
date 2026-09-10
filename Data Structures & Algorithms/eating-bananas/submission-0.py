class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """"""
        left_k=1
        right_k=max(piles)
        result=0
        while left_k<=right_k:
            hours_took=[]

            mid_k = ((left_k + right_k) // 2)
            for p in piles:
                hours_took.append(math.ceil(p/mid_k))
            hours=sum(hours_took)

            if hours <= h:
                result=mid_k
                right_k=mid_k-1
            else:
                left_k=mid_k+1

        return result