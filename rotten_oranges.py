from collections import deque


class Solution:
    def orangesRotting(self, grid):
        number_to_state = {
            'empty': 0,
            'fresh': 1,
            'rotten': 2
        }

        n_rows = len(grid)
        n_cols = len(grid[0])

        def is_all_empty():
            for i in range(n_rows):
                for j in range(n_cols):
                    if grid[i][j] != number_to_state['empty']:
                        return False

            return True

        def get_neighbors(row, col):
            potential_neighs = [
                (row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)
            ]
            neighs = []

            for potential_row, potential_col in potential_neighs:
                if (0 <= potential_row < n_rows and
                        0 <= potential_col < n_cols and
                        grid[potential_row][potential_col] == number_to_state['fresh']):
                    neighs.append((potential_row, potential_col))

            return neighs
            
        def get_time_to_rot_oranges(starting_oranges):
            discovered = set()
            queue = deque()
            time = -1

            for orange in starting_oranges:
                discovered.add(orange)
                queue.append(orange)

            while queue:
                work_nodes = []
                while queue:
                    work_nodes.append(queue.popleft())

                neighbors = []
                for work_node in work_nodes:
                    neighbors += get_neighbors(work_node[0], work_node[1])

                for neigh in neighbors:
                    if neigh not in discovered:
                        discovered.add(neigh)
                        queue.append(neigh)
                        grid[neigh[0]][neigh[1]] = number_to_state['rotten']

                time += 1

            return time

        if is_all_empty():
            return 0

        def has_fresh_oranges():
            for i in range(n_rows):
                for j in range(n_cols):
                    if grid[i][j] == number_to_state['fresh']:
                        return False

            return True

        rotten_indexes = []
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == number_to_state['rotten']:
                    rotten_indexes.append((i, j))

        time = get_time_to_rot_oranges(rotten_indexes)

        return time if has_fresh_oranges() else -1
