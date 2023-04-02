# <><><><><><><><><><><>Queue with Linked List<><><><><><><><><><><>
"""
시간 복잡도 1로 만들기 위해서 linked list로 구현
"""
import sys


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue():

    def __init__(self):
        self.f = None
        self.r = None
        self.num = 0

    # push 함수
    def push(self, x: int):
        temp = Node(x)
        if not self.f:
            self.f = self.r = temp
        else:
            self.r.next = temp
            self.r = temp
        self.num += 1

    # pop 함수
    def pop(self):
        if self.num == 0:
            print(-1)
            return
        print(self.f.data)
        temp = self.f
        self.f = temp.next
        self.num -= 1

    # size 함수
    def size(self):
        print(self.num)

    # empty 함수
    def empty(self):
        print(1 if self.num == 0 else 0)

    # front 함수
    def front(self):
        if self.num == 0:
            print(-1)
            return
        print(self.f.data)

    # back 함수
    def back(self):
        if self.num == 0:
            print(-1)
            return
        print(self.r.data)


queue = Queue()
# 명령어 미리 저장
case = {
    "pop": lambda queue: queue.pop(),
    "size": lambda queue: queue.size(),
    "empty": lambda queue: queue.empty(),
    "front": lambda queue: queue.front(),
    "back": lambda queue: queue.back()
}

n = int(input())
for _ in range(n):
    # 명령 수가 많아서 sys로 받음
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        queue.push(int(command[1]))
    else:
        case[command[0]](queue)


#<<><><><><><><><><><><>Queue with List<><><><><><><><><><><>
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
