/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  const stack = [];
  const openings = [
    '(', '[', '{'
  ];

  for(let i = 0; i < s.length; i++) {
    if(openings.includes(s[i])) {
      stack.push(s[i]);
    } else if (stack.length > 0) {
      const char = stack.pop();
      if(char === '(' && s[i] !== ')') return false;
      if(char === '[' && s[i] !== ']') return false;
      if(char === '{' && s[i] !== '}') return false;
    } else {
      return false;
    }
  }

  return stack.length === 0;
};