class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total_sum = 0
        # for i in nums:
        #     sum += int(max(str(i)) * len(str(i)))
        # return sum

        
        for num in nums:
            max_digit = 0
            temp = num
            count = 0

            while temp>0:
                digit = temp%10
                max_digit = max(max_digit,digit)
                count += 1
                temp //= 10
            
            encrypted = 0

            for i in range(count):
                encrypted = encrypted*10 + max_digit
            total_sum += encrypted

        return total_sum 