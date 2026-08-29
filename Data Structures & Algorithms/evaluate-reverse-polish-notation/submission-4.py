class Solution:
    def __init__(self):
        self.tokens=['+', '-', '/', '*']
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:return 0

    def evaluate_expression(self, operator, num1, num2):
        if operator == '+':return num1+num2
        elif operator == '-':return num1-num2
        elif operator == '/':return int(num1/num2)
        else:return num1*num2

    def evalRPN(self, tokens: list[str]) -> int:
        """"""
        for item in tokens:
            if item not in self.tokens:
                self.push(item)
            elif item in self.tokens:
                num_2=self.top()
                self.pop()
                num_1=self.top()
                self.pop()
                result=self.evaluate_expression(item, int(num_1), int(num_2))
                self.push(str(result))
        return int(self.top())