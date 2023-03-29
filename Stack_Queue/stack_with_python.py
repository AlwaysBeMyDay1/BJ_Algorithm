# 스택
class Stack():
    listed_stack = []
    def push(self, X):
        self.listed_stack.append(X)
        
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.listed_stack.pop(-1)
    
    def size(self):
        return len(self.listed_stack)
    
    def empty(self):
        return 1 if len(self.listed_stack) == 0 else 0
        
    def top(self):
        if self.empty():
            return -1
        else:
            return self.listed_stack[-1]

def make_stack():
    stack = Stack()

    N = int(input())

    order_list = []
    for i in range(N):
        order_list.append(input())

    for order in order_list:
        if order.startswith('push'):
            push_num = int(order.split()[1])
            stack.push(push_num)
        elif order.startswith('top'):
            print(stack.top())
        elif order.startswith('size'):
            print(stack.size())
        elif order.startswith('empty'):
            print(stack.empty())
        elif order.startswith('pop'):
            print(stack.pop())

make_stack()
    