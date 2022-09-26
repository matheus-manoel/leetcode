class Solution:
    def dfs(self, grid, row, col, visited):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[row])):
            return

        if grid[row][col] != 1:
            return

        visited.add((row, col))

        for i in [-1, 1]:
            new_row = row + i
            if (new_row, col) not in visited:
                self.dfs(grid, new_row, col, visited)

        for i in [-1, 1]:
            new_col = col + i
            if (row, new_col) not in visited:
                self.dfs(grid, row, new_col, visited)

    def numIslands(self, grid):
        visited = set()
        n_of_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    n_of_islands += 1
                    self.dfs(grid, row, col, visited)

        return n_of_islands
