class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=="+":
                first=stack.pop()
                second=stack.pop()
                stack.append(int(second)+int(first))
            elif token=="-":
                first=stack.pop()
                second=stack.pop()
                stack.append(int(second)-int(first))
            elif token=="*":
                first=stack.pop()
                second=stack.pop()
                stack.append(int(second)*int(first))
            elif token=="/":
                first=stack.pop()
                second=stack.pop()
                stack.append(int(int(second)/int(first)))
            else:
                stack.append(int(token))
        return stack[0]
        