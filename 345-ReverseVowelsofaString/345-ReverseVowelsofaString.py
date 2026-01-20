# Last updated: 20/1/2026, 12:50:32 p. m.
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels = "aeiou"
4        vwls = [v for v in s if v.lower() in vowels]
5        s = list(s)
6
7        result = []
8        for c in s:
9            if c.lower() in vowels:
10                v = vwls.pop()
11                result.append(v)
12            else:
13                result.append(c)
14        return "".join(result)
15
16
17
18
19
20        return result
21
22        