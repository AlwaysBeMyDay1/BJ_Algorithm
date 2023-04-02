import sys


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class Deque():

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


deque = Deque()
# 명령어 미리 저장
case = {
    "pop_front": lambda deque: deque.pop_front(),
    "pop_back": lambda deque: deque.pop_back(),
    "size": lambda deque: deque.size(),
    "empty": lambda deque: deque.empty(),
    "push_front": lambda deque: deque.push_front(),
    "push_back": lambda deque: deque.push_back()
}

n = int(input())
for _ in range(n):
    # 명령 수가 많아서 sys로 받음
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        deque.push(int(command[1]))
    else:
        case[command[0]](deque)