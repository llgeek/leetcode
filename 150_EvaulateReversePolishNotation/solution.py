class Solution:
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        stack = []
        #opeset = {'+', '-', '*', '/'}
        opeset = {'+': lambda x, y : x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: int(x/y)}
        try:
            for s in tokens:
                if s in opeset:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(opeset[s](num2, num1))
                else:
                    stack.append(int(s))
            return stack[0]
        except ValueError:
            print("Invalid input") 

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))