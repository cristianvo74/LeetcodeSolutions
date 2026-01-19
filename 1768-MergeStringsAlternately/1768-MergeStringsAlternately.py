# Last updated: 19/1/2026, 1:35:51 p. m.
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        max_lenght = max(len(word1), len(word2))
4        new_word = ""
5        for i in range(max_lenght):
6            if i < len(word1):
7                a = word1[i]
8            if i < len(word2):
9                b = word2[i]
10            new_word += a
11            new_word += b
12            a, b = "", ""
13        return new_word
14