class Solution:
    def lengthOfLIS(self, nums):
        def get_lis_starting_at(index, memo):
            if index in memo:
                return memo[index]
            
            local_lis = 1
            for j in range(index + 1, len(nums)):
                if nums[j] > nums[index]:
                    local_lis = max(local_lis, 1 + get_lis_starting_at(j, memo))

            memo[index] = local_lis
            return local_lis

        cache = {len(nums) - 1: 1}
        lis = 1
        for i in range(len(nums) - 1, -1, -1):
            lis = max(lis, get_lis_starting_at(i, cache))

        return lis

class Solution:
    def lengthOfLIS(self, nums):
        def get_lis_starting_at(index, memo):
            local_lis = 1
            for j in range(index + 1, len(nums)):
                if nums[j] > nums[index]:
                    local_lis = max(local_lis, 1 + memo[j])

            memo[index] = local_lis
            return local_lis

        cache = {len(nums) - 1: 1}
        lis = 1
        for i in range(len(nums) - 1, -1, -1):
            lis = max(lis, get_lis_starting_at(i, cache))

        return lis
