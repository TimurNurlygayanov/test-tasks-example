

class Node(object):
    next = None
    previous = None

    def __init__(self, value):
        self.value = value


# Stack - FIFO
class Stack(object):
    head = None
    tail = None
    size = 0

    def push(self, value):
        node = Node(value)

        if self.tail:
            node.previous = self.tail
            self.tail.next = node

        self.tail = node

        if not self.head:
            self.head = node

        self.size += 1

    def pop(self):
        last_node = self.tail
        self.tail = self.tail.previous
        self.tail.next = None

        self.size -= 1

        return last_node.value


# LIFO
class Queue(object):
    head = None
    tail = None
    size = 0

    def push(self, value):
        node = Node(value)

        if self.tail:
            node.previous = self.tail
            self.tail.next = node

        self.tail = node

        if not self.head:
            self.head = node

        self.size += 1

    def pop(self):
        first_node = self.head
        self.head = self.head.next
        self.head.previous = None

        self.size -= 1

        return first_node.value


# test Stack:
print('Testing Stack FIFO')
s = Stack()
for i in range(10):
    s.push(i)
for i in range(5):
    print(s.pop())


# test Queue:
print('Testing Queue LIFO')
s = Queue()
for i in range(10):
    s.push(i)
for i in range(5):
    print(s.pop())

