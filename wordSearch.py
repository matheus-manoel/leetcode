class Solution:
    def __init__(self):
        self.is_word_in_board = False

    def dfs(self, board, row, col, word, index_word, visited):
        if not (0 <= row < len(board) and 0 <= col < len(board[row])):
            return

        if word[index_word] != board[row][col]:
            return

        if len(word) == index_word + 1:
            self.is_word_in_board = True
            return

        visited.add((row, col))

        for i in [-1, 1]:
            next_row = row + i
            if (next_row, col) not in visited:
                self.dfs(board, next_row, col, word, index_word + 1, visited)
        for i in [-1, 1]:
            next_col = col + i
            if (row, next_col) not in visited:
                self.dfs(board, row, next_col, word, index_word + 1, visited)

        visited.remove((row, col))

    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[row])):
                self.dfs(board, row, col, word, 0, set())

        return self.is_word_in_board
