'''
class Solution:
    def __init__(self):
        self.max_depth = 0

    def _get_max_depth(self, node, depth):
        if not node:
            return

        self.max_depth = max(self.max_depth, depth)

        self._get_max_depth(node.left, depth + 1)
        self._get_max_depth(node.right, depth + 1)

    def maxDepth(self, root):
        self._get_max_depth(root, 1)
        return self.max_depth
'''


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
