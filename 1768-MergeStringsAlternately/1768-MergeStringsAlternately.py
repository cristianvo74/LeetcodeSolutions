# Last updated: 19/1/2026, 2:11:04 p. m.
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        min_l = min(len(word1), len(word2))
4
5        new_w = []
6        for a,b in zip(word1, word2):
7            new_w.append(a)
8            new_w.append(b)
9        new_w += word1[min_l:].split()
10        new_w += word2[min_l:].split()
11        new_w = "".join(new_w)
12
13        return new_w