from collections import deque


class Solution:
    def coinChange(self, coins, amount):
        def get_fewest_number_of_coins_to_amount(cur_amount, memo=None):
            if memo is None:
                memo = {0: 0}

            if cur_amount in memo:
                return memo[cur_amount]

            ans = []
            can_be_made = False
            for coin in coins:
                new_amount = cur_amount - coin
                if new_amount >= 0:
                    res = get_fewest_number_of_coins_to_amount(new_amount, memo)
                    if res != -1:
                        ans.append(res)
                        can_be_made = True

            memo[cur_amount] = min(ans) + 1 if can_be_made else -1

            return memo[cur_amount]

        return get_fewest_number_of_coins_to_amount(amount)

    def coinChange2(self, coins, amount):
        q = deque()
        discovered = set()
        distances = {}

        discovered.add(0)
        q.append(0)
        distances[0] = 0

        while q:
            work_node = q.popleft()

            for neigh in map(lambda coin: coin + work_node, coins):
                if neigh <= amount and neigh not in discovered:
                    discovered.add(neigh)
                    distances[neigh] = distances[work_node] + 1
                    q.append(neigh)

        return distances[amount] if amount in distances else -1
