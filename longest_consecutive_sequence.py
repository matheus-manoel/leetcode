class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        used = set()
        max_seq = 0

        for num in nums:

            if num not in used:
                seq = 1

                prev = num - 1
                while prev in nums_set:
                    seq += 1
                    used.add(prev)
                    prev -= 1

                next = num + 1
                while next in nums_set:
                    seq += 1
                    used.add(next)
                    next += 1

                max_seq = max(max_seq, seq)

        return max_seq
