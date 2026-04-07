class Stack:
    #сам стек
    def __init__(self):
        self.stack = []

    #положить элемент в стек
    def push(self, elem):
        self.stack.append(elem)

    #взять элемент из стека
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    #элемент на вершине
    def peek(self):
        if self.stack:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    
    #размер стека
    def size(self):
        return len(self.stack)
    
    #является ли стек пустым
    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True


def isCorrect(s):
    stack = Stack()
    for el in s:
        if el in ['[', '{', '(']:
            stack.push(el)
        elif (el == ']') and (stack.peek() == '['):
            stack.pop()
        elif (el == ')') and (stack.peek() == '('):
            stack.pop()
        elif (el == '}') and (stack.peek() == '{'):
            stack.pop()
        else:
            return 'Неверная последовательность'
    if stack.isEmpty():
        return 'Верная последовательность'
    else:
        return 'Неверная последовательность'

def Buildings(arr):
    stack = Stack()
    stack.push(arr[0])
    for el in arr:
        if el > stack.peek():
            stack.push(el)
    return stack.peek()

def Fib(n):
    stack1 = Stack()
    stack2 = Stack()
    stack1.push(1)
    stack2.push(1)
    
    for i in range(1, n):
        fib = stack1.peek() + stack2.peek()
        stack1.push(stack2.peek())
        stack2.push(fib)
    
    return stack2.peek()


stack = Stack()
stack.push(5)
print(stack.stack)