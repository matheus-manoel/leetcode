class Solution:

    def nearestPalindromic(self, n):
        if int(n) <= 11:
            for res in range(9, -1, -1):
                if res < int(n):
                    return str(res)

        if (int(n) + 1) % 10 == 0:
            return str(int(n) + 2)

        if len(n) % 2 == 0:
            first_half = n[:int(len(n) / 2)]

            variations = []
            diffs = []

            variation_1 = first_half + first_half[::-1]
            variations.append(variation_1)
            diffs.append(abs(int(n) - int(variation_1)))

            base_for_variation_2 = str(int(first_half) + 1)
            variation_2 = base_for_variation_2 + base_for_variation_2[::-1]
            variations.append(variation_2)
            diffs.append(abs(int(n) - int(variation_2)))

            base_for_variation_3 = str(int(first_half) - 1)
            variation_3 = base_for_variation_3 + base_for_variation_3[::-1]
            variations.append(variation_3)
            diffs.append(abs(int(n) - int(variation_3)))

            min_diff = float('inf')
            min_variation = ''
            for i, diff in enumerate(diffs):
                if diff <= min_diff and diff != 0:
                    min_diff = diff
                    min_variation = variations[i]

            print(variations)
            print(diffs)

            return min_variation



print(Solution().nearestPalindromic(input()))
