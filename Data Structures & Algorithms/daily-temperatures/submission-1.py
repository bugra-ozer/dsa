from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_deque=deque()
        result=[0]*len(temperatures)
        for idx in range(len(temperatures)):
            while temp_deque and temperatures[idx]>temperatures[temp_deque[-1]]:
                prev_idx = temp_deque.pop()
                result[prev_idx]=idx-prev_idx
            temp_deque.append(idx)
        return result