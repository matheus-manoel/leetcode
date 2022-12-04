from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        m = len(heights)
        n = len(heights[0])

        def get_neighbors(node):
            row, col = node
            neighs = []
            for new_row, new_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= new_row < m and 0 <= new_col < n and heights[new_row][new_col] <= heights[row][col]:
                    neighs.append((new_row, new_col))

            return neighs

        def can_flow_to_both_oceans(src_row, src_col, memo):
            can_flow_lt = False
            can_flow_rb = False

            q = deque()
            discovered = set()
            q.append((src_row, src_col))
            discovered.add((src_row, src_col))

            while q:
                work_node = q.popleft()

                if work_node in memo:
                    return True
                if work_node[1] == 0 or work_node[0] == 0:
                    can_flow_lt = True
                if work_node[1] == n - 1 or work_node[0] == m - 1:
                    can_flow_rb = True
                if can_flow_lt and can_flow_rb:
                    return True

                for neigh in get_neighbors(work_node):
                    if neigh not in discovered:
                        discovered.add(neigh)
                        q.append(neigh)

            return False

        can_flow = []
        memo = set()
        for i in range(m):
            for j in range(n):
                if can_flow_to_both_oceans(i, j, memo):
                    can_flow.append([i, j])
                    memo.add((i, j))

        return can_flow
