# Last updated: 20/1/2026, 1:21:20 p. m.
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        s = s.split()
4        s = s[::-1]
5        s = " ".join(s)
6        return s