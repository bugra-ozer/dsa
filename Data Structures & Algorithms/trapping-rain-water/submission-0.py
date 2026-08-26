class Solution:
    def trap(self, height: List[int]) -> int:
        result = []
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        for index in range(len(height)):
            left_max[index] = max(left_max[index-1], height[index])
        right_max[len(height) - 1]=height[len(height) - 1]
        for index in range(len(height) - 2, -1, -1):
            right_max[index] = max(right_max[index + 1], height[index])
        for index in range(len(height)):
            result.append(min(left_max[index],right_max[index])-height[index])
        return sum(result)