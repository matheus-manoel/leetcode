from collections import deque


class Solution:
    def levelOrder(self, root):
        ans = []
        q = deque()

        if root:
            q.append({'node': root, 'level': 0})

        current_level = 0
        level_ans = []
        while len(q):
            elem = q.popleft()
            node, level = elem['node'], elem['level']

            if level == current_level:
                level_ans.append(node.val)
            else:
                ans.append(level_ans)
                current_level += 1
                level_ans = [node.val]

            if node.left:
                q.append({'node': node.left, 'level': level + 1})
            if node.right:
                q.append({'node': node.right, 'level': level + 1})

        if level_ans:
            ans.append(level_ans)

        return ans
