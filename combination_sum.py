class Solution:
    def combinationSum(self, candidates, target):
        def combination_sum(candidates, my_target, combination, response):
            if my_target == 0:
                response.append(combination)

            for candidate in candidates:
                if my_target == target:
                    combination = []
                next_number = my_target - candidate
                if next_number >= 0:
                    combination.append(candidate)
                    combination_sum(candidates, next_number, combination, response)

        response = []
        combination_sum(candidates, target, [], response)

        print(response)
        return response
