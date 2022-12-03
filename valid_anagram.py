from collections import Counter
import string

class Solution:
    def isAnagram(self, s, t):
        s_counter = Counter(s)
        t_counter = Counter(t)

        for letter in string.string.ascii_lowercase:
            if s_counter[letter] != t_counter[letter]:
                return False

        return True

        '''
        s = 'caar'
        s_counter = {
            'c': 1,
            'a': 2,
            'r': 1,
        }
        '''
