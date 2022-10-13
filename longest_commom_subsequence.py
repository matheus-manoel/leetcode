class Solution:
    def longestCommonSubsequence(self, text1, text2):
        def lcs(index_1, index_2, memo):
            if index_1 < 0 or index_2 < 0:
                return 0

            if (index_1, index_2) in memo:
                return memo[(index_1, index_2)]

            if text1[index_1] == text2[index_2]:
                memo[(index_1, index_2)] = lcs(index_1 - 1, index_2 - 1, memo) + 1
            else:
                memo[(index_1, index_2)] = max(
                    lcs(index_1, index_2 - 1, memo),
                    lcs(index_1 - 1, index_2, memo)
                )

            return memo[(index_1, index_2)]

        return lcs(len(text1) - 1, len(text2) - 1, {})
