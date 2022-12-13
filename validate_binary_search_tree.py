# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):

        def is_valid_bst(node, lower, upper):
            if lower < node.val < upper:
                valid_left = is_valid_bst(node.left, lower, node.val) if node.left else True
                valid_right = is_valid_bst(node.right, node.val, upper) if node.right else True

                return valid_left and valid_right

            return False

        return is_valid_bst(root, -float('inf'), float('inf'))
