# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                return cur


'''
This functions but space complexity is O(log n):

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        p_list = []
        q_list = []

        node = root
        while node.val != p.val:
            p_list.append(node)
            if node.val < p.val:
                node = node.right
            else:
                node = node.left
        p_list.append(node)

        node = root
        while node.val != q.val:
            q_list.append(node)
            if node.val < q.val:
                node = node.right
            else:
                node = node.left
        q_list.append(node)

        lca = None
        for p_candidate, q_candidate in zip(p_list, q_list):
            if p_candidate.val == q_candidate.val:
                lca = p_candidate

        return lca
'''
