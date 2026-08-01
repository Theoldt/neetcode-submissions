class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            "o": ["(","[","{"],
            "c": [")","]","}"],
        }

        corresponding = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        remains = []


        for char in s:
            if len(remains) == 0 and char in bracket["c"]:
                return False
            elif char in bracket["o"]:
                remains.append(char)
            elif remains[-1] == corresponding[char]:
                remains.pop()
            else:
                return False

        if len(remains) > 0:
            return False
        else:
            return True
                
                


        