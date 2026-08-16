class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        s = []


        for t in tokens:
            if t == "+":
                w = int(s.pop())
                calc = int(s[-1]) + w
                s.pop()
                s.append(calc)
            elif t == "-":
                w = int(s.pop())
                calc = int(s[-1]) - w
                s.pop()
                s.append(calc)
            elif t == "*":
                w = int(s.pop())
                calc = int(s[-1]) * w
                s.pop()
                s.append(calc)
            elif t == "/":
                w = int(s.pop())
                calc = int(s[-1]) / w
                s.pop()
                s.append(int(calc))
            else:
                s.append(t)

        return int(s[0])









        