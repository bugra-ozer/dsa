import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums=nums
        self.k=k
        while len(self.nums)>k:
            self.popHeap()

    def popHeap(self):
        return heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        print(self.nums)
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.k:
            self.popHeap()
        return self.nums[0]

