class Solution:
    def countSubstrings(self, s):
        def is_palindrome(st, start, end, memo):
            if end - start == 0:
                return True

            if end - start == -1:
                return st[start] == st[end]

            if (start, end) in memo:
                return memo[(start, end)]

            memo[(start, end)] = st[start] == st[end] and is_palindrome(st, start + 1, end - 1, memo)

            return memo[(start, end)]

        cache = {}
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_palindrome(s, i, j, cache):
                    count += 1

        return count
