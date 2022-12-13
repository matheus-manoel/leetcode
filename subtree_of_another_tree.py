# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        def is_subtree(node, subroot_node):
            if not node and not subroot_node:
                return True

            if not node or not subroot_node:
                return False

            if node.val == subroot_node.val:
                return (
                    is_subtree(node.left, subroot_node.left) and
                    is_subtree(node.right, subroot_node.right)
                )

            return False

        def contains_subtree(node):
            if node is None:
                return False

            if is_subtree(node, subRoot):
                return True

            return contains_subtree(node.left) or contains_subtree(node.right)

        return contains_subtree(root)
