class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        ast = 0
        for i in s:
            if count % 2 == 0 and i == "*":
                ast += 1
            if i == "|":
                count += 1
        return ast