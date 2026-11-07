class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # if num % 10 == 0 and num != 0:
        #     return False
        # r_num = str(num)[::-1]
        # return int(r_num[::-1]) == num

        return num % 10 != 0 or num == 0