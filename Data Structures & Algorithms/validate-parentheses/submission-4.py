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

        stack = []


        for char in s:
            if len(stack) == 0 and char in bracket["c"]:
                return False
            elif char in bracket["o"]:
                stack.append(char)
            elif stack[-1] == corresponding[char]:
                stack.pop()
            else:
                return False

        if len(stack) > 0:
            return False
        else:
            return True
                
                


        