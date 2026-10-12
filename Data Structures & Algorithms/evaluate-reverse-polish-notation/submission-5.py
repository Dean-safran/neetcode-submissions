class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens : 
            if token in ops :
                right = stack[-1]
                left = stack[-2]
                del stack[-1]
                del stack[-1]
                if token == "+" :
                    stack.append(left + right)
                elif token == "-" :
                    stack.append(left - right)
                elif token == "/" :
                    stack.append(int(left / right))
                elif token == "*" :
                    stack.append(left * right)
            else : 
                stack.append(int(token))

        return stack[0]