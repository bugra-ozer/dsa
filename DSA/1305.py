# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
class Solution:
    def getAllElements(self, root1, root2) -> list[int]:
        result = []

        def get_elements(node, result: list):
            if node.val is not None: result.append(node.val)

            if node.left is not None: get_elements(node.left, result)
            if node.right is not None: get_elements(node.right, result)

        if root1 is not None: get_elements(root1, result)
        if root2 is not None: get_elements(root2, result)
        return sorted(result)