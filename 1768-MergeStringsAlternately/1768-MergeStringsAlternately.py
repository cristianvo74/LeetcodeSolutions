# Last updated: 19/1/2026, 2:15:34 p. m.
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        min_l = min(len(word1), len(word2))
4        new_w = []
5        for a,b in zip(word1, word2):
6            new_w.append(a)
7            new_w.append(b)
8        new_w.append(word1[min_l:])
9        new_w.append(word2[min_l:]) 
10        return "".join(new_w)