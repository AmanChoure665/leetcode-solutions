class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        
        a,b,c = nums[0],nums[1],nums[2]
        if a<b<c or c<b<a:
            return b
        elif c<a<b or b<a<c:
            return a
        else:
            return c
        