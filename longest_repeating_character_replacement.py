class Solution:
    def characterReplacement(self, s, k):
        def get_max_frequence(frequences):
            return max(frequences.values())

        def get_initial_frequences():
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            return {char: 0 for char in chars}

        frequences = get_initial_frequences()
        size_longest_substring = 0
        left = 0
        for right in range(len(s)):
            frequences[s[right]] += 1
            substring_len = right - left + 1

            while substring_len - get_max_frequence(frequences) > k:
                frequences[s[left]] -= 1
                left += 1
                substring_len -= 1

            size_longest_substring = max(
                    size_longest_substring,
                    substring_len
            )

        return size_longest_substring


Solution().characterReplacement("AABABBA", 1)
