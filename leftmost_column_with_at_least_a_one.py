# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        [n, m] = binaryMatrix.dimensions()

        left_most_i = float('inf')

        def binary_search(row, lo, hi, row_left_most_memo=None):
            if row_left_most_memo is None:
                row_left_most_memo = [float('inf')]

            if lo <= hi:
                mid = int((lo + hi)/2)
                num = binaryMatrix.get(row, mid)
                if num:
                    row_left_most_memo[0] = mid
                    return binary_search(row, lo, mid - 1, row_left_most_memo)
                else:
                    return binary_search(row, mid + 1, hi, row_left_most_memo)

            return row_left_most_memo[0]

        for i in range(n):
            row_left_most_i = binary_search(i, 0, m-1)
            if row_left_most_i < left_most_i:
                left_most_i = row_left_most_i

        return left_most_i if left_most_i != float('inf') else -1
