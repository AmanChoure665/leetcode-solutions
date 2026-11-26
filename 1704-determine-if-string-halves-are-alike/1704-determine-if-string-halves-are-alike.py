class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        mid = len(s)//2

        # approach 1
        # a = 0
        # b = 0
        # for i in range(mid):
        #     if s[i] in vowels:
        #         a += 1
        # for j in range(mid,n):
        #     if s[j] in vowels:
        #         b += 1
        # return a == b

        #approach 2
        count = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                count += 1 if i < mid else -1
        return count == 0

        #approach 3
        # a = sum(ch in vowels for ch in s[:mid])
        # b = sum(ch in vowels for ch in s[mid:])
        # return a==b