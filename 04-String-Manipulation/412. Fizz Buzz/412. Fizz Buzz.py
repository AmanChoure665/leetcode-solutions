1class Solution:
2    def fizzBuzz(self, n: int) -> list[str]:
3        answer = []
4        
5        for i in range(1, n+1):
6            if i % 3 == 0 and i % 5 == 0:
7                answer.append(FizzBuzz)
8            elif i % 3 == 0:
9                answer.append(Fizz)
10            elif i % 5 ==0:
11                answer.append(Buzz)
12            else:
13                answer.append(str(i))
14
15        return answer