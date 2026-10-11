class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            total = 0
            for d in str(num):
                total += int(d)
            num = total
        return num