class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(i)

            while len(stack) > 0 and t > temperatures[stack[-1]]:
                w = stack.pop()
                calc = i - w
                result[w] = calc
            else:
                stack.append(i)

        return result


