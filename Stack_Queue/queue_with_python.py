# 큐
class Queue():
    listed_queue = []

    def push(self, X):
        self.listed_queue.append(X)

    def pop(self):
        return -1 if self.empty() else self.listed_queue.pop(0)

    def size(self):
        return len(self.listed_queue)

    def empty(self):
        return 1 if len(self.listed_queue) == 0 else 0

    def front(self):
        return -1 if self.empty() else self.listed_queue[0]

    def back(self):
        return -1 if self.empty() else self.listed_queue[-1]


def make_queue():
    queue = Queue()

    N = int(input())

    order_list = []
    for _ in range(N):
        order_list.append(input())

    for order in order_list:
        if order.startswith('push'):
            push_num = int(order.split()[1])
            queue.push(push_num)
        elif order.startswith('front'):
            print(queue.front())
        elif order.startswith('back'):
            print(queue.back())
        elif order.startswith('size'):
            print(queue.size())
        elif order.startswith('empty'):
            print(queue.empty())
        elif order.startswith('pop'):
            print(queue.pop())


make_queue()