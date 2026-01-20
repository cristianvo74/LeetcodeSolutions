# Last updated: 20/1/2026, 2:05:34 a. m.
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        max_val = max(candies)
4        result = []
5        for kid in candies:
6            if kid + extraCandies >= max_val:
7                result.append(True)
8            else:
9                result.append(False)
10        return result
11        