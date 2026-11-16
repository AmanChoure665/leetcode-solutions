class Solution(object):
    def alternateDigitSum(self, n):
        res = 0
        sign = 1
        while n:
            res += n % 10 * sign
            sign = -sign
            n //= 10

        return res * -sign