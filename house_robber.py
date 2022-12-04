class Solution:
    def rob(self, nums):
        def get_max_starting_at(starting_index, memo):
            if starting_index in memo:
                return memo[starting_index]

            max_at_index = nums[starting_index]

            for i in range(starting_index + 2, len(nums)):
                sum = get_max_starting_at(i, memo) + nums[starting_index]
                max_at_index = max(max_at_index, sum)

            memo[starting_index] = max_at_index

            return max_at_index

        global_max = nums[len(nums) - 1]
        memo = {}
        for i in range(len(nums) - 1, -1, -1):
            max_at_index = get_max_starting_at(i, memo)
            global_max = max(max_at_index, global_max)

        return global_max
