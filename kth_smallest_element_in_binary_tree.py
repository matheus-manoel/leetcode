# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        position = 1

        def get_kth_smallest(node):
            if node is None:
                return node

            if node.left:
                return get_kth_smallest(node.left)

            nonlocal position
            if k == position:
                return node
            position += 1

            if node.right:
                return get_kth_smallest(node.right)

        return get_kth_smallest(root).val
