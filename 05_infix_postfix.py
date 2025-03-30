class Stack:
    def __init__(self):
        self.data=[]
    
    def isEmpty(self):
        return len(self.data)==0
    
    def push(self,data):
        self.data.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        raise Exception("Stack is empty")
    
    def peek(self):
        if not self.isEmpty():
            return self.data[-1]
        raise Exception("Stack is empty")
    
class Queue:
    def __init__(self):
        self.data =[]

    def isEmpty(self):
        return len(self.data)==0
    
    def enqueue(self,data):
        self.data.append(data)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)#for FIFO pop(0)
        raise Exception("Queue is Empty")
    
    def __str__(self):
        return ' '.join(self.data)
    
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3

def associativity(op):
    if op in ('+','-','*','/'):
        return 'L'
    else:
        return 'R'

def shunting_yard(inifx):
    operator_stack=Stack()
    output_queue=Queue()
    tokens=inifx.replace('(', ' ( ').replace(')', ' ) ')

    for token in tokens:
        if token.isalnum():
            output_queue.enqueue(token)
        elif token== '(':
            operator_stack.push(token)
        elif token== ')':
            while not operator_stack.isEmpty() and operator_stack.peek()!='(':
                output_queue.enqueue(operator_stack.pop())
            if not operator_stack.isEmpty():
                operator_stack.pop()
        elif token in ('+','-','*','/','^'):
            while(not operator_stack.isEmpty() and operator_stack.peek()!='(' and precedence(operator_stack.peek()>precedence(token) or precedence(operator_stack.peek()==precedence(token) and associativity(token)=='L'))):
                output_queue.enqueue(operator_stack.pop())
            operator_stack.push(token)
    while not operator_stack.isEmpty():
        output_queue.enqueue(operator_stack.pop())
    
    return str(output_queue)

if __name__=="__main__":
    inifx=input("Enter an expression: ")
    postfix_expression=shunting_yard(inifx)
    print(f"Postfix Expression: {postfix_expression}")