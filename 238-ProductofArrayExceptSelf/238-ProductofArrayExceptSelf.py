# Last updated: 22/1/2026, 12:09:14 p. m.
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        pre = [1] * n
5        suf = [1] * n
6        for i in range(1, n):
7            pre[i] = nums[i-1] * pre[i-1]
8        
9        for i in range(-2, -n-1, -1):
10            suf[i] = nums[i+1] * suf[i+1]
11
12        result = [1]*n
13        for i in range(n):
14            result[i] = pre[i] * suf[i]
15        return result
16        
17        