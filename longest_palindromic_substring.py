'cabas'
0, 1, 2, 3, 4


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(starting_index, last_index):
            '''
                'aba' -> len = 3 -> 3/2 -> 1, from 0 -> 1 (non inc), checking
                         if s[i] == s[last_index - i]
                'abcba' -> len = 5 -> 5/2 -> 2, from 0 -> 2 (non inc), checking
                         if s[i] == s[last_index - i]
                'abba'  -> len = 4 -> 4/2 -> 2, from 0 -> 2 (non inc)
            '''
            size_str = last_index - starting_index + 1
            middle = size_str // 2 + starting_index

            j = 0
            for i in range(starting_index, middle):
                if s[i] != s[last_index - j]:
                    return False
                j += 1

            return True

        def recursive_is_palindrome(starting_index, last_index, memo):
            if (starting_index, last_index) in memo:
                return memo[(starting_index, last_index)]

            if starting_index >= last_index:
                memo[(starting_index, last_index)] = True
                return True

            memo[(starting_index, last_index)] = s[starting_index] == s[last_index] and recursive_is_palindrome(starting_index + 1, last_index - 1, memo)
            return memo[(starting_index, last_index)]

        longest_palindrome_length = 0
        longest_palindrome_indexes = None
        memo = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if recursive_is_palindrome(i, j, memo) and j - i + 1 > longest_palindrome_length:
                    longest_palindrome_length = j - i + 1
                    longest_palindrome_indexes = (i, j)

        if longest_palindrome_indexes:
            return s[longest_palindrome_indexes[0]:longest_palindrome_indexes[1] + 1]

        return ''
