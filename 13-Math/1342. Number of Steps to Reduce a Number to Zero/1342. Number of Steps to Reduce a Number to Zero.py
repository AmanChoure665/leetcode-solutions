1class Solution:
2    def numberOfSteps(self, num: int) -> int:
3        step = 0
4        while num > 0:
5            if num % 2 == 0:
6                num //= 2
7            else:
8                num -= 1
9            step +=1
10        return step