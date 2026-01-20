# Last updated: 20/1/2026, 2:30:46 a. m.
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        counter = 0
4
5        for i in range(len(flowerbed)):
6            if i == 0 and flowerbed[i] == 0 and len(flowerbed) == 1:
7                counter += 1
8            elif i == 0 and flowerbed[i] == 0 and flowerbed[1] == 0:
9                flowerbed[i] = 1
10                counter += 1
11            elif i > 0 and i < (len(flowerbed) - 1) and flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
12                flowerbed[i] = 1
13                counter += 1
14            elif i == (len(flowerbed) - 1) and flowerbed[i] == 0 and flowerbed[i-1] == 0:
15                flowerbed[i] = 1
16                counter += 1
17        if n <= counter:
18            return True
19        else:
20            return False