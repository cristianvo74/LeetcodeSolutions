# Last updated: 19/1/2026, 1:58:29 p. m.
# Using list instead of strings
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        len_1 = len(word1)
4        len_2 = len(word2)
5
6        if len_1 <= len_2:
7            min_l = len_1
8            max_w = word2
9        else:
10            min_l = len_2
11            max_w = word1
12
13        new_w = []
14        for i in range(min_l):
15            a = word1[i]
16            b = word2[i]
17            new_w.append(a)
18            new_w.append(b)
19        new_w = "".join(new_w)
20        new_w += max_w[i+1:]
21
22        return new_w