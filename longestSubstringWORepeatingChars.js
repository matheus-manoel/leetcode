/*Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.*/

const getLongestSubstringWORepeatinChars = (s) => {
  const charPresence = {}
  let longestSubstring = 0;
  let windowStart = 0;

  for(windowEnd = 0; windowEnd < s.length; windowEnd++) {
    if (charPresence[s[windowEnd]] === undefined) {
      charPresence[s[windowEnd]] = 1;
    } else {
      charPresence[s[windowEnd]] += 1;
    }
    
    while(charPresence[s[windowEnd]] > 1) {
      charPresence[s[windowStart]] -= 1;
      windowStart += 1;
    }

    longestSubstring = Math.max(longestSubstring, windowEnd - windowStart  + 1);
  }

  return longestSubstring;
}

console.log(getLongestSubstringWORepeatinChars('abcabcbb'));
console.log(getLongestSubstringWORepeatinChars("bbbbb"));
console.log(getLongestSubstringWORepeatinChars("pwwkew"));
