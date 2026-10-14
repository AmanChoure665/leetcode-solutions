class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for chr in address:
            if chr == ".":
                result += "[.]"
            else:
                result += chr
        return result