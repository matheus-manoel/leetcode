class Solution:
    def rob(self, nums):
        def get_max_starting_at(starting_index, max_index, memo):
            if starting_index in memo:
                return memo[starting_index]

            max_at_index = nums[starting_index]

            for i in range(starting_index + 2, max_index):
                sum = get_max_starting_at(i, max_index, memo) + nums[starting_index]
                max_at_index = max(max_at_index, sum)

            memo[starting_index] = max_at_index

            return max_at_index

        global_max = nums[len(nums) - 1]
        memo = {}
        for i in range(len(nums) - 1, -1, -1):
            max_at_index = get_max_starting_at(i, len(nums) - 1, memo)
            global_max = max(max_at_index, global_max)

        global_max_2 = nums[len(nums) - 2]
        memo = {}
        for i in range(len(nums) - 1, 0, -1):
            max_at_index = get_max_starting_at(i, len(nums), memo)
            global_max_2 = max(max_at_index, global_max_2)

        return max(global_max, global_max_2)



class Solution2:
    '''
    [200, 3, 140, 20, 10]
    [
        max(200, 200) = 200,
        max(3, 200) = 200,
        max(140 + 200, 200) = 340,
        max(20 + 200, 340) = 340,
        max(10 + 340, 340) = 350
    ]
    '''
    def rob(self, nums):

        def get_max_money_from_rob(houses):
            n_houses = len(houses)

            max_at_house_i = []
            for i in range(n_houses):
                rob_house_in_i = nums[i] + max_at_house_i[i - 2] if i - 2 >= starting_index else nums[i]
                dont_rob_house_in_i = nums[i-1] if i-1 >= 0 else 0
                max_at_house_i.append(max(rob_house_in_i, dont_rob_house_in_i))

            return max(max_at_house_i)

        return max(get_max_money_from_rob(houses[:-1]), get_max_money_from_rob(houses[1:]))
