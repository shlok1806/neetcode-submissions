class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        # last in first out 

        for op in operations : 
            if op == "+" :
                res += int (stack[-1] + stack[-2])

                stack.append(stack[-1] + stack[-2])
            elif op == "D" :
                res += int (stack[-1] * 2)
                stack.append(stack[-1] * 2)
            elif op == "C" :
                
                res -= stack.pop()
            else : 
                stack.append(int (op))
                res += int (op)


        return res
