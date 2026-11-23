class Solution:
    def checkString(self, s: str) -> bool:
        total_a = s.count("a")
        fre = 0
        for i in s:
            if i == "b":
                break
            else:
                fre += 1
        if fre == total_a:
            return True
        else:
            return False
