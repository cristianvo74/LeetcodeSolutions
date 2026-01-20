# Last updated: 20/1/2026, 1:56:03 a. m.
1class Solution:
2    def gcdOfStrings(self, str1: str, str2: str) -> str:
3        for i in range(len(str1), 0 , -1):
4            candidate = str1[:i]
5            if len(str2) % i == 0:
6                if str2 == candidate * (len(str2)//len(candidate)) and str1 == candidate * (len(str1)//len(candidate)):
7                    return candidate
8        return ""