class Solution:
    def _get_traversed_order_and_direction(self, node, direction):
        if not node:
            return []

        ans = []
        ans += self._get_traversed_order_and_direction(node.left, 'left')
        ans += self._get_traversed_order_and_direction(node.right, 'right')

        ans.append((node.val, direction))

        return ans

    def isSameTree(self, p, q):
        p_t_and_d = self._get_traversed_order_and_direction(p, None)
        q_t_and_d = self._get_traversed_order_and_direction(q, None)

        return p_t_and_d == q_t_and_d
