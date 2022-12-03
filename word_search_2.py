class Solution:
    def findWords(self, board, words):
        def build_trie():
            trie = {'is_leaf': False}

            for word in words:
                current_node = trie
                for c in word:
                    if c not in current_node:
                        current_node[c] = {'is_leaf': False}
                    current_node = current_node[c]
                current_node['is_leaf'] = True

            return trie

        def remove_from_trie(trie, word):
            curr = trie
            stack = []
            
            for ch in word:
                stack.append(curr)
                curr = curr[ch]
            curr['is_leaf'] = False

            for t_node, ch in reversed(list(zip(stack, word))):
                if len(t_node[ch]) > 1:  # has children
                    return
                else:
                    del t_node[ch]
            '''
            current = trie
            stack = []
            for c in word:
                current = current[c]
                stack.append(current)

            i = len(stack) - 1
            while stack:
                current = stack.pop()
                if i + 1 == len(word):
                    current['is_leaf'] = False
                    if len(current.keys()) > 1:
                        break
                else:
                    if len(current[word[i + 1]].keys()) == 2:
                        del current[word[i + 1]]
                i -= 1
            '''


        def is_in_limit(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        result = set()

        def dfs(trie_root, row, col, trie, path, visited=None):
            if visited is None:
                visited = set()

            if (row, col) in visited or trie is None:
                return

            if trie['is_leaf']:
                result.add(path)
                remove_from_trie(trie_root, path)

            visited.add((row, col))

            directions = [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]

            for new_row, new_col in directions:
                if is_in_limit(new_row, new_col):
                    next_char = board[new_row][new_col]
                    dfs(trie_root, new_row, new_col, trie.get(next_char, None), path + next_char, visited)

            visited.remove((row, col))

        trie = build_trie()

        for i in range(len(board)):
            for j in range(len(board[i])):
                next_char = board[i][j]
                if next_char in trie:
                    dfs(trie, i, j, trie[next_char], next_char)

        return [*result]
