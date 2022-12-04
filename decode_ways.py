class Solution:
    def numDecodings(self, s: str) -> int:
        def count_ways(st, memo):
            if st == len(s) - 1:
                return 1

            if st in memo:
                return memo[st]

            possibility_1 = s[st+1] if st+1 < len(s) else None
            possibility_2 = s[st+1:st+3] if st+2 < len(s) else None
            n_ways = 0
           
            if possibility_1 and possibility_1 != '0':
                n_ways += count_ways(st + 1, memo)

            if possibility_2 and possibility_2[0] != '0' and 1 <= int(possibility_2) <= 26:
                n_ways += count_ways(st + 2, memo)

            memo[st] = n_ways
            return n_ways

        memo = {}
        return count_ways(-1, memo)
