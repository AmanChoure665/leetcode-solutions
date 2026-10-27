class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        digit_sum = 0
        for num in str(n):
            product *= int(num)
            digit_sum += int(num)
        return product-digit_sum