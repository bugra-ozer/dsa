# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]

# Instinct
# Missing reasoning: BST is already sorted, maybe not same as a list being sorted, but sorted regardless.
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

# main
class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:

        def get_elements(node: TreeNode, result:list=None):
            if result is None: result=[]
            if node.left is not None: get_elements(node.left, result)
            if node.val is not None: result.append(node.val)
            if node.right: get_elements(node.right, result)
            return result

        if (not root1 and not root2): return []
        if not root1: return get_elements(root2)
        if not root2: return get_elements(root1)

        if root1 is not None:
            res_one = []
            res_one = get_elements(root1, res_one)
        if root2 is not None:
            res_two = []
            res_two = get_elements(root2, res_two)

        result = []
        i, j = 0, 0
        while (i < len(res_one) and j < len(res_two)):
            if res_one[i] <= res_two[j]:
                result.append(res_one[i])
                i += 1
            else:
                result.append(res_two[j])
                j += 1

        # one of the lists ran out.
        result.extend(res_one[i:])
        result.extend(res_two[j:])
        return result