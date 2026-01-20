# Last updated: 20/1/2026, 2:08:04 a. m.
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        max_val = max(candies)
4        return [kid + extraCandies >= max_val for kid in candies]