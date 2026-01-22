# Last updated: 22/1/2026, 12:22:59 p. m.
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        result = [1]*n
5
6        #Pre
7        for i in range(1, n):
8            result[i] = nums[i-1] * result[i-1]
9        
10        #Suf
11        R = 1
12        for i in range(n-1, -1, -1):
13            result[i] = result[i] * R
14            R *= nums[i]
15            
16        return result
17        
18        