from collections import deque


class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        discovered = set([node])
        to_visit = deque()
        to_visit.append(node)

        old_to_new = {node: Node(node.val)}

        while to_visit:
            work_node = to_visit.popleft()
            new_node = old_to_new[work_node]

            for neighbor in work_node.neighbors:
                if neighbor not in discovered:
                    discovered.add(neighbor)
                    to_visit.append(neighbor)
                    old_to_new[neighbor] = Node(neighbor.val)
                new_node.neighbors.append(old_to_new[neighbor])

        return old_to_new[node]
